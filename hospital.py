import pymysql
import random
# σημείωση να αντικατασταθεί με το socket file που ορίζεται στο config

def main_menu():
    print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
    print('1: Πληροφοριες γαι τη ΒΔ (οι πίνακες της ΒΔ)')
    print('2: Εισαγωγή ασθενη στη νοσηλευτικη μοναδα')
    print('3: Καταχώρηση ασθενή σε θάλαμο')
    print('4: Εξιτηριο ασθενή από θάλαμο και πληρωμή')
    print('5: Θάλαμος νοσηλείας κάποιου ασθενή')
    print('6: Σημειώσεις ασθενών')
    print('7: Ιατροί ανα κλινική')
    print('8: Iατροί ανα ασθενή')
    print('9: Νοσοκομειακό προσωπικό που επιβλέπει κάθε κλινική')
    print('10: Πληροφορίες για την αποθήκη κάθε κλινικης')
    print('11: Ασθενοφορα για χρηση')
    answer = ' '
    while not answer in '1 2 3 4 5 6 7 8 9 10 11'.split():
        answer = input('επιλογή.....')
        if answer == '': return 0
    else:
        return answer

def storageroom_menu():
    print('\nΠΛΗΡΟΦΟΡΙΕΣ ΓΙΑ ΤΙΣ ΑΠΟΘΗΚΕΣ (enter για έξοδο)')
    print('1: Πληροφοριες γαι τα φαρμακα')
    print('2: Πληροφοριες γαι τα ιατρικα εργαλεια')
    print('3: Πληροφοριες γαι τις πρωτες υλες')
    answer = ' '
    while not answer in '1 2 3'.split():
        answer = input('επιλογή.....')
        if answer == '': return 0
    else:
        return answer

def takedata():
        con = pymysql.connect(host = 'localhost',\
                     user='root', passwd=None, db='hosp', charset='utf8')
        cur = con.cursor()
        cur.execute('select version()')
        buffer = ""
        print (" Δώστε εντολές SQL (enter για έξοδο)")
        #while True:
        line = input('>>>')
        buffer += line
        print (buffer)
        if True: 
                try:
                    buffer = buffer.strip()
                    if buffer.lstrip().upper().startswith("SELECT"):
                        count=0
                        s=10
                        cur.execute(buffer)
                        desc = [x[0] for x in cur.description]
                        print(*desc, sep='\t')
                        for row in cur.fetchall():
                            for i in row :
                                print ('%8s'%i, end = '\t')
                            print()
                            count +=1
                    else:
                        cur.execute(buffer)
                        cur.execute('commit')
                    mylist.insert(END,"σύνολο :" +str(cur.rowcount))
                    print ("σύνολο :", cur.rowcount )
                except pymysql.Error as e:
                    print ("An error occurred:", e)
                buffer = ""
        cur.execute('commit')        
        con.close()
        
def printTables():
    print("ΟΙ ΠΙΝΑΚΕΣ ΠΟΥ ΥΠΑΡΧΟΥΝ ΣΕ ΑΥΤΗ ΤΗ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΤΟΥ ΝΟΣΟΚΟΜΕΙΟΥ ΕΙΝΑΙ ΟΙ ΕΞΗΣ:")
    print('\n')
    cur =con.cursor()
    cur.execute("SHOW TABLES")
    i=0
    for row in cur.fetchall():
        print (row)#,'\n')#, end = '\t')
        i=i+1
    print("\n ΣΥΝΟΛΙΚΑ",i,"ΠΙΝΑΚΕΣ")

def insertPatient():
        print("\n Δώστε τα στοιχεία του ασθενή")
        id_astheni = input("give id_astheni: ")
    #try:
        cur = con.cursor()
        cur.execute ("SELECT if( '%s' not in( SELECT id_astheni from asthenis),'το συστημα επεξεργαζεται τα δεδομένα..','λάθος id_astheni');"%id_astheni)
        for row in cur.fetchall():
            for i in row :
                j=i
            #print()
            #print(i)
        #print()
        con.commit()
        if(j=='το συστημα επεξεργαζεται τα δεδομένα..'):
            firstname = input("give firstname: ")
            lastname = input("give lastname: ")
            hlikia = input("give hlikia: ")
            dieuthinsi = input("give dieuthinsi: ")
            fulo = input("give fulo: ")
            phone_num = input("give phone_num: ")
            cur.execute (" INSERT INTO asthenis(id_astheni,firstname,lastname,hlikia,dieuthinsi,fulo,phone_num) VALUES (%s,%s,%s,%s,%s,%s,%s) ",
                         (id_astheni,firstname,lastname,hlikia,dieuthinsi,fulo,phone_num))
            con.commit()
            print("you have done an insert operation succesfully..!")
        else:
            print(" O κωδικός ασθενή που δώσατε υπάρχει ήδη, ξαναπροσπαθήστε..")
            insertPatient()
    #except:
     #   print("something going wrong...")
def DoctorsPerClinic():
    print("\n ΟΙ ΙΑΤΡΟΙ ΚΑΘΕ ΚΛΙΝΙΚΗΣ ΕΙΝΑΙ ΟΙ ΕΞΗΣ: \n")
    try:
        cur = con.cursor()
        cur.execute (" SELECT id_ergazomenou,firstname,lastname,eidikothta_klinikis FROM `ergazomenos` join anhkei on ergazomenos.id_ergazomenou=anhkei.id_giatrou ORDER by anhkei.eidikothta_klinikis")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
        #print("you have done an insert operation succesfully..!")
    except:
        print("something going wrong...")


def CheckInPatient():
#αρχικα ελεγχει αν το id που δινουμε ειναι γραμμενο σαν ασθενης στη βαση και αν ειναι οτι δεν νοσηλευεται ηδη(μπορει να ηταν παλια στη βαση),αν οχι ξαναζηταει id
#μετα αφου δωσουμε κλινικη βρισκει τους ελευθερους θαλαμους της κλινικης που θελουμε να εισαγουμε τον ασθενη
#αφου δωσουμε εναν θαλαμο απο τους ελευθερους εισαγει τον ασθενη σε αυτον
#επειτα βρισκει τους γιατρους της κλινικης εισαγωγης και τυχαια βαζει εναν να τον παρακολουθει
#τελος με τυχαιο τροπο εισαγει δεδομενα στο αρχειο ιστορικου του νοσοκομειου για αυτον τον ασθενη
    
    asthenis=input("id ασθενή : ")
    cur = con.cursor() #elenxei an einai grammenos sto susthma kai an den noshleuetai idi - gia tuxon lathi
    #cur.execute ("SELECT IF('%s' in(SELECT id_astheni FROM asthenis)  AND '%s' not in(SELECT asthenis.id_astheni from asthenis join noshleuetai on asthenis.id_astheni=noshleuetai.id_astheni),'id_astheni αποδεκτό..','please insert the personal information of patient first-go to step 2'); "%(asthenis,asthenis))
    #cur.execute ("SELECT IF('%s' in(SELECT id_astheni FROM asthenis)  AND '%s' in(SELECT pairnei_eksithrio.id_astheni from pairnei_eksithrio where datediff(pairnei_eksithrio.hmeromhnia_eksagwghs,curdate())<0 or datediff(pairnei_eksithrio.hmeromhnia_eksagwghs,curdate())=0),'id_astheni αποδεκτό..','λαθος id'); "%(asthenis,asthenis))
    cur.execute("select if('%s' in(SELECT id_astheni from asthenis) and '%s' not in(SELECT id_astheni from noshleuetai where id_astheni not IN( SELECT id_astheni FROM pairnei_eksithrio) OR id_astheni IN( SELECT id_astheni FROM pairnei_eksithrio WHERE (hmeromhnia_eksagwghs IS NULL OR DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURRENT_DATE)>0))),'id_astheni αποδεκτό..','λαθος id')"%(asthenis,asthenis))


    for row in cur.fetchall():
        for i in row :
            print()
            print(i)
        print()
    con.commit()
    if(i=='id_astheni αποδεκτό..'):
        print("ΤΟ ΣΥΣΤΗΜΑ ΚΑΤΑΛΑΒΑΙΝΕΙ ΤΙΣ ΚΛΙΝΙΚΕΣ ΑΥΣΤΗΡΑ ΩΣ ΕΞΗΣ : \npathologiki,geniki xeirourgiki,ourologiki,kardiologiki,dermatologiki\nneurologiki,gunaikologiki,wtorinolaruggologiki,plastiki xeirourgiki\npneumonologiki\n")
        kliniki=input("κλινική εισαγωγής : ")
        print( "Τα ελεύθερα δωμάτια της κλινικής είναι τα εξής :")
        cur = con.cursor() # briskei ta eleuthera dwmatia , auta diladi pou den einai sto left join pairnei eksithrio me hmeromhnia
        #eite null( an kserei esk arxhs pote feugei mporei na to balei) eite me hmeromhnia mikroteri ti current--diladi na exei adeiasei
        cur.execute ("SELECT thalamos.id_thalamou FROM THALAMOS WHERE eidikothta_klinikis='%s' AND id_thalamou not IN(SELECT NOSHLEUETAI.id_thalamou FROM noshleuetai left JOIN pairnei_eksithrio ON noshleuetai.id_thalamou = pairnei_eksithrio.id_thalamou where pairnei_eksithrio.hmeromhnia_eksagwghs IS NULL OR DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURDATE())>0)"%kliniki) 
       
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        for row in cur.fetchall():
            for i in row :
                print ('%8s'%i, end = '\t')
            print()
        con.commit()

        thalamos=input("θάλαμος εισαγωγής : ") #kapoion apo tous parapanw pou tha parw
        cur = con.cursor()
        cur.execute ("INSERT into noshleuetai(id_astheni,id_thalamou,hmeromhnia_eisagwghs) VALUES ('%s','%s',CURDATE())"%(asthenis,thalamos))
        con.commit()
        print( "o ασθενης με κωδικό %s νοσηλευεται στο θάλαμο %s της κλινικής %s"%(asthenis,thalamos,kliniki))

        cur = con.cursor() # briskei tous giatrous tis klinikis pou nosileuetai
        cur.execute (" SELECT id_ergazomenou FROM `ergazomenos` join anhkei on ergazomenos.id_ergazomenou=anhkei.id_giatrou WHERE anhkei.eidikothta_klinikis='%s'"%kliniki)
        print()
        giatros=[]
        for row in cur.fetchall():
            for i in row :
                giatros.append(i)
            print()
        con.commit()
        iatros=giatros[random.randint(0,(len(giatros)-1))] # dialegw enan tuxaia kai meta ton bazw na parakolouthei ton astheni

        cur = con.cursor()
        cur.execute ("INSERT into parakoloythei(id_astheni,id_ergazomenou) VALUES ('%s','%s')"%(asthenis,iatros))
        con.commit()
        print( "o ασθενης με κωδικό %s θα παρακολουθείται από τον γιατρό με κωδικό %s"%(asthenis,iatros))
        # twra pairname sto istoriko shmeiwseis
        shmeiwseis=['αθλείται','καπνίζει','πάσχει από άγνοια','έχει αλλεργία στις κορτιζόνες','έχει ψυχολογικά προβλήματα','πάσχει από χρόνια ασθένεια',
                    'πάσχει από διαβήτη','έχει παλινδρόμηση','έχει θυροειδή','πάσχει από κατάθλιψη','είναι τυφλός','είναι κουφός',
                    'είναι ανάπηρος','αναζητείται','πάσχει από αλκοολισμό','είναι υπέρβαρος']
        shmeiwseisAstheni=''
        
        for i in range(0,random.randint(0,3)):
            shmeiwseisAstheni=shmeiwseisAstheni+str(shmeiwseis[random.randint(0,len(shmeiwseis)-1)])+str(' , ')
        cur = con.cursor()
        cur.execute ("SELECT id_ergazomenou FROM `proswpiko_grammateias`")
        grammateia=[]
        for row in cur.fetchall():
            for i in row :
                grammateia.append(i)
        con.commit()
        proswpikogrammateias=grammateia[random.randint(0,len(grammateia)-1)]
        id_istorikou="ist"+str(random.randint(0,1000))+str(asthenis)
        cur = con.cursor()
        cur.execute ("INSERT into istoriko_grammateias(id_astheni,id_istorikou,shmeiwseis,id_ergazomenou) VALUES ('%s','%s','%s','%s')"%(asthenis,id_istorikou,shmeiwseisAstheni,proswpikogrammateias))
        con.commit()
    else:
        print( "Λάθος κωδικός ασθενή, είτε δεν έχει καταγραφεί σαν ασθενής (βήμα 2) , είτε νοσηλευέται ήδη...Ξαναπροσπαθήστε")
        CheckInPatient()
    
def CkeckOutPatientAndPuy():
#αρχικα ελεγχει αν το id που δινουμε  νοσηλευεται αυτη τη στιγμη,αν οχι καλειται παλι η συναρτηση μονη της
#αν ναι του δινουμε εξιτηριο με ημερομηνια εξαγωγης την τωρινη.
#τελος με τυχαιο τροπο υπολογιζει ενα ποσο πληρωμης, εξαρτωμενο απο τυχαιο πολλαπλασιαστη ανα ημερα νοσηλειας,
#και βαζει δεδομενα στο πινακα λογαριασμος πληρωμης για τον ασθενη που πηρε εξιτηριο

###αρχικα μου δινει τους εν ενεργεια ασθενεις που νοσηλευονται για να γλυτωσω τα λαθη,-  na ftiaksw edw mesa kai to parakolouthei ,notes tuxaia, epiblepei na to balw standar apo eks arxhs
##    #print("Oι ασθενείς που νοσηλεύονται αυτή τι στιγμή είναι οι εξής : ")
##    #cur = con.cursor() #pairnw osous nosileuontai auth th stigmh gia na apofugw lathos id
##    #cur.execute ("SELECT id_astheni from noshleuetai where id_astheni not IN(SELECT id_astheni FROM pairnei_eksithrio) OR id_astheni IN(SELECT id_astheni FROM pairnei_eksithrio WHERE (hmeromhnia_eksagwghs IS NULL OR DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURRENT_DATE)>0))")
##    #desc = [x[0] for x in cur.description]
##    #print(*desc, sep='\t')
##    #for row in cur.fetchall():
##    #    for i in row :
##    #        print ('%8s'%i, end = '\t')
##    #    print()
##    #con.commit()
    
    asthenis=input("id ασθενή : ") #ena apo ta parapanw
    cur = con.cursor() #pairnw osous nosileuontai auth th stigmh gia na apofugw lathos id
    cur.execute ("select if (('%s' in(SELECT id_astheni from asthenis) and '%s' not IN(SELECT id_astheni FROM pairnei_eksithrio)) OR ('%s' in(SELECT id_astheni from asthenis) and '%s' IN(SELECT id_astheni FROM pairnei_eksithrio WHERE (hmeromhnia_eksagwghs IS NULL OR DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURRENT_DATE)>0))),'id_astheni αποδεκτό..','error');"%(asthenis,asthenis,asthenis,asthenis))
    for row in cur.fetchall():
        for i in row :
            print()
            print(i)
        print()
    con.commit()
    if(i=='id_astheni αποδεκτό..'):
        cur.execute ("INSERT into pairnei_eksithrio(id_astheni,id_thalamou,hmeromhnia_eksagwghs) VALUES ('%s',(SELECT id_thalamou FROM noshleuetai WHERE id_astheni='%s'),CURDATE())"%(asthenis,asthenis))
        con.commit()
        print("\nO ασθενής με κωδικό %s πήρε εξιτήριο \n"%asthenis)
        print("Ωρα για πληρωμη...")
        prices=[20,25,30,40,45,50,60,70,75,100,150,200,300] #tuxaies times ,paei timh*meres
        priceperday=prices[random.randint(0,12)]
        apodeikseis=['asdfewsf','tayfgdsh','safeqfqe','eqffeqfq','qwertyuj','plkmiuy','345tgyiuw','uyqtgcyuq','iueu66e','qazwwsx','mnhtyr','mhgruouy','ppllkkmb']
        apodeiksi=apodeikseis[random.randint(0,12)]+str(asthenis)# gia na einai panta monadiko
        #print(priceperday,apodeiksi)
        cur = con.cursor() #pairnw poses meres noshleuetai kai briskw ti total timi
        row = cur.execute ("select datediff(pairnei_eksithrio.hmeromhnia_eksagwghs,noshleuetai.hmeromhnia_eisagwghs)*'%s' from pairnei_eksithrio JOIN noshleuetai on pairnei_eksithrio.id_astheni=noshleuetai.id_astheni WHERE pairnei_eksithrio.id_astheni='%s'"%(priceperday,asthenis))
        for row in cur.fetchall():
            for i in row :
               totalprice=i+20
        con.commit()
        cur = con.cursor()
        cur.execute ("INSERT INTO logariasmos_plhrwmhs(id_astheni,timh,apodeiksi_plhrwmhs) VALUES('%s','%s','%s');"%(asthenis,totalprice,apodeiksi))
        con.commit()    
        print("..............")
        print("Λογαριασμός εξοφλήθηκε \n Tιμή : '%s'  \n Απόδειξη : '%s'"%(totalprice,apodeiksi))
    else:
        print( "Λάθος κωδικός ασθενή, είτε δεν έχει καταγραφεί σαν ασθενής (βήμα 2) , είτε δεν νοσηλευέται ακόμη...Ξαναπροσπαθήστε")
        CkeckOutPatientAndPuy()

def freeAmbulance():
    print("\n Ελεύθερα ασθενοφόρα: \n")
    try:
        cur = con.cursor()
        cur.execute ("SELECT arithmos_pinakidas FROM asthenoforo WHERE asthenoforo.diathesimo=1")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")

           
def informationForStorageRoom():
#με το 1 παιρνω τα φαρμακα ανα αποθηκη κλινικης που ειναι σε ποσοτητα κατω απο 30
#με το 2 παιρνω τα ιατρικα-εργαλεια ανα αποθηκη κλινικης που ειναι σε ποσοτητα κατω απο 30
#με το 3 παιρνω τις πρωτες υλες ανα αποθηκη κλινικης που ειναι σε ποσοτητα κατω απο 30
                       
    while True:
        information = storageroom_menu()
        if information == '1': medicinesToBuyPerClinic()
        elif information == '2': IatrikaErgaleiaPerClinic()
        elif information == '3': PrwtesUlesPerClinic()
        a=input("\nΘέλετε να κάνετε και άλλη αναζήτηση ?  (y/n)")
        if a=='y':
                continue
        else:
                break


def medicinesToBuyPerClinic():
    print("\n φαρμακα που ειναι σε ποσοτητα κατω απο 30 ανα κλινικη: \n")
    try:
        cur = con.cursor()
        cur.execute ("SELECT farmako.id_apothikis,farmako.onoma_farmakou,farmako.posothta_se_apothema,apothiki.eidikothta_klinikis FROM farmako join apothiki on farmako.id_apothikis=apothiki.id_apothikis WHERE posothta_se_apothema<30 ORDER BY `farmako`.`id_apothikis`")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")

def IatrikaErgaleiaPerClinic():
    print("\n ιατρικα εργαλεια που ειναι σε ποσοτητα κατω απο 30 ανα κλινικη: \n")
    try:
        cur = con.cursor()
        cur.execute ("SELECT iatrika_ergaleia.id_apothikis,iatrika_ergaleia.iatriko_ergaleio,iatrika_ergaleia.apothema,apothiki.eidikothta_klinikis FROM iatrika_ergaleia join apothiki on iatrika_ergaleia.id_apothikis=apothiki.id_apothikis WHERE apothema<30 ORDER BY `iatrika_ergaleia`.`id_apothikis`")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")

def PrwtesUlesPerClinic():
    print("\n πρωτες υλες που ειναι σε ποσοτητα κατω απο 30 ανα κλινικη: \n")
    try:
        cur = con.cursor()
        cur.execute ("SELECT prwtes_ules.id_apothikis,prwtes_ules.prwth_ulh,prwtes_ules.apothema,apothiki.eidikothta_klinikis FROM prwtes_ules join apothiki on prwtes_ules.id_apothikis=apothiki.id_apothikis WHERE apothema<30 ORDER BY `prwtes_ules`.`id_apothikis`")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")

def DoctorsPerPatient():
    print("\nοι ιατροί παρακολουθουν τους εξής ασθενής: \n")
    try:
        cur = con.cursor() 
        #cur.execute ("SELECT * FROM `parakoloythei` WHERE 1 ORDER by id_ergazomenou")
        #auto mou dinei kai osous htan palia sto noshleuetai gia to arxeio p krataw, isws tha mporousa me to pou parei kapoios eksithrio na
        #ton svhnw kai apo ti bash meta,alla to thewrw pio swsto na menei ws istoriko
        #gia auto kanw select sto parakoloythei na tupwsei mono osous einai akoma se noshleia kai den phran eksithrio
        #bazw to hmeromhnia_ekasgwghs is null kai ta upoloipa mhn tuxon uparxei kapoios pou kserei apo meres prin pote bgainei, na kalipsw kai auth th periptwsh
        cur.execute("SELECT parakoloythei.id_ergazomenou,parakoloythei.id_astheni FROM parakoloythei join noshleuetai on parakoloythei.id_astheni=noshleuetai.id_astheni where noshleuetai.id_astheni not in (SELECT pairnei_eksithrio.id_astheni from pairnei_eksithrio join noshleuetai on pairnei_eksithrio.id_astheni=noshleuetai.id_astheni where pairnei_eksithrio.hmeromhnia_eksagwghs is null or DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURDATE())<0 OR DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURDATE())=0)")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")
def NursesPerClinic():
    print("\n νοσοκομομειακο προσωπικο που επιβλεπει τους θαλάμους και τις αποθήκες κάθε κλινικής : \n")
    try:
        cur = con.cursor()
        cur.execute ("SELECT * FROM `epiblepei` WHERE 1 ORDER by eidikothta_klinikis")
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    except:
        print("something going wrong...")

def findRoomOfPatient():
    asthenis=input("id ασθενή : ")
    cur = con.cursor() #elenxei an einai grammenos sto susthma kai an den noshleuetai idi - gia tuxon lathi
    cur.execute ("SELECT IF('%s' in (SELECT id_astheni from asthenis) and '%s' in (SELECT id_astheni from noshleuetai) and '%s' not in(SELECT pairnei_eksithrio.id_astheni from pairnei_eksithrio join noshleuetai on pairnei_eksithrio.id_astheni=noshleuetai.id_astheni where pairnei_eksithrio.hmeromhnia_eksagwghs is null or DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURDATE())<0 or DATEDIFF(pairnei_eksithrio.hmeromhnia_eksagwghs,CURDATE())=0),'το συστημά επεξεργάζεται τα δεδομένα..','λάθος id_astheni-δεν υπάρχει ασθενής με τέτοιο κωδικό \n \t\tπου να νοσηλεύεται αυτή τη στιγμή'); "%(asthenis,asthenis,asthenis))    
    for row in cur.fetchall():
        for i in row :
            print()
            print(i)
        print()
    con.commit()
    if(i=='το συστημά επεξεργάζεται τα δεδομένα..'):
        
        cur.execute("SELECT noshleuetai.id_astheni,noshleuetai.id_thalamou,thalamos.eidikothta_klinikis FROM noshleuetai JOIN thalamos ON noshleuetai.id_thalamou=thalamos.id_thalamou where noshleuetai.id_astheni='%s'"%asthenis) 
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    else:
        print( "Λάθος κωδικός ασθενή, είτε δεν έχει καταγραφεί σαν ασθενής (βήμα 2) , είτε δεν νοσηλευέται ακόμα...Ξαναπροσπαθήστε")
        findRoomOfPatient()
    
def NotesPerPatient():
    asthenis=input("id ασθενή : ")
    cur = con.cursor() #elenxei an einai grammenos sto susthma
    cur.execute ("SELECT IF('%s' in (SELECT id_astheni from asthenis) and '%s'!='','το συστημά επεξεργάζεται τα δεδομένα..','λάθος id_astheni-δεν υπάρχει ασθενής με τέτοιο κωδικό \n \t\tπου να νοσηλεύεται αυτή τη στιγμή');"%(asthenis,asthenis))
    # για εναν πολυ περιεργο λογο η πανω εντολη χωρις το and '%s'!='' δεν ετρεχε για ορισματα asthenis=a10,a11,a12 και γενικα με 3 χαρακτηρες εδω στη python
    #ενώ για μικροτερα ετρεχε (πχ asthenis=a1)
    #ενώ στο php my admin ετρεχε κανονικα για ολα. Δεν ξερω τι παιζει , το and '%s'!='' ειναι ξεκαθαρα για να γλυτωσω το ερρορ που ανεφερα και για κανενα αλλο λογο,
    for row in cur.fetchall():
        for i in row :
            print()
            print(row)
        print()
    con.commit()
    if(i=='το συστημά επεξεργάζεται τα δεδομένα..'):
        cur.execute("SELECT istoriko_grammateias.id_astheni,istoriko_grammateias.id_istorikou,istoriko_grammateias.shmeiwseis FROM istoriko_grammateias where istoriko_grammateias.id_astheni='%s'"%asthenis) 
        desc = [x[0] for x in cur.description]
        print(*desc, sep='\t')
        print()
        for row in cur.fetchall():
            for i in row :
                    print ('%8s'%i, end = '\t')
            print()
        con.commit()
    else:
        print( "Λάθος κωδικός ασθενή, είτε δεν έχει καταγραφεί σαν ασθενής (βήμα 2) , είτε δεν νοσηλευέται ακόμα...Ξαναπροσπαθήστε")
        NotesPerPatient()
h = 'localhost'
while True:
    try:
        print("Αίτημα σύνδεσης με τη Βάση δεδομένων του νοσοκομείου... ")
        con = pymysql.connect(host = h,user='root', passwd=None, db='hosp', charset='utf8')
    except pymysql.Error as e:
        print ('Σφάλμα', e)
    else:
        con.isolation_level = None
        cur = con.cursor()
        cur.execute('select version()')
        print('Επιτυχής σύνδεση \nΕκδοση βάσης δεδομένων: {}'.format(cur.fetchone()))
        print()
        break
buffer = ""


if con:
    print ("Ακολουθούν μερικές βασικές λειτουργίες - πληροφορίες για κάθε νοσοκομείο")
    while True:
        answer = main_menu()
        if not answer: break
        elif answer == '1': printTables()
        elif answer == '2': insertPatient()
        elif answer == '3': CheckInPatient() 
        elif answer == '4': CkeckOutPatientAndPuy()
        elif answer == '5': findRoomOfPatient()
        elif answer == '6': NotesPerPatient()
        elif answer == '7': DoctorsPerClinic()
        elif answer == '8': DoctorsPerPatient()        
        elif answer == '9': NursesPerClinic()
        elif answer == '10': informationForStorageRoom()
        elif answer == '11': freeAmbulance()
