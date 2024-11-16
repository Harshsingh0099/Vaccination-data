import mysql.connector

class Database_Helper:
    
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            port="3306",
            password="ez@45)678Z",
            database="vaccine"
        )

        str_query = "create table if not exists vaccination(Student_ID int primary key, Student_Name varchar(100), Phone_Number varchar(12), student_grade varchar(7), vaccination_Status varchar(3))"
        mycursor = self.con.cursor()
        mycursor.execute(str_query)
     
    
    
    def insert_Data(self, id, name, phone, grade, dose):
        str_query="insert into vaccination(Student_ID, Student_Name, Phone_Number, student_grade, vaccination_Status) values({},'{}','{}','{}','{}')".format(id,name,phone, grade, dose)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Report {} saved to Database".format(name))


    
    def fetch_data(self):
        str_query="select * from vaccination"
        cur=self.con.cursor()
        cur.execute(str_query)
        for record in cur:
            print(f"Student_ID: {record[0]}")
            print(f"Student_name: {record[1]}")
            print(f"Student_Phone: {record[2]}")
            print(f"student_grade: {record[3]}")
            print(f"vaccination Status: {record[4]}")
            
            print()
            print()


    
    def delete(self,id):
        str_query="delete from student where Student_ID = {}".format(id)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student with id {} is deleted\n".format(id))
     


    
    def update_User(self,id,newname, newphone, grades, doses):
        str_query="update student set Student_Name='{}', Phone_Number='{}', student_grade='{}', vaccination_status='{}' where Student_ID={}".format(newname, newphone, grades, doses,id)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student with Id {} updated\n".format(id))
     
 



if __name__ == "__main__":
    db=Database_Helper()
    print("***** WELCOME TO VACCINATION STATUS REPORT *****")
    while(True):
        print("Press 1 to insert new Student")
        print("Press 2 to display all Students")
        print("Press 3 to delete a Student")
        print("Press 4 to update a Student")
        print("Press 5 to exit the program")
        try:
            choice=int(input())

            if(choice==1):
                
                uid=int(input("Enter Student ID: "))
                uname=input("Enter Student Name: ")
                uphone=input("Enter Student's Phone: ")
                ugrade=input("Enter Student's grade: ")
                ustatus=input("Enter vaccination Status.'1' for partialy vaccinated and '2' for fully vaccinated: ")[0]
                db.insert_Data(uid,uname, uphone, ugrade,ustatus)
                pass


            elif choice==2:
                
                db.fetch_data()
                pass


            elif choice==3:
                
                uid=int(input("Enter ID to be deleted: "))
                db.delete(uid)
                pass


            elif choice==4:
               
                uid=int(input("Enter Student ID: "))
                uname=input("Enter new name: ")
                uphone=input("Enter new phone number: ")
                ugrade=input("Enter Student's new grade: ")
                ustatus=input("Enter new vaccination Status. '1' for partially vaccinted and '2' for fully vaccinated: ")
                db.update_User(uid,uname,uphone,ugrade,ustatus)


            elif choice==5:
                break


            else:
                print("Invalid input! Please try again")
                
                
        except Exception as e:
            print(e)
            print("Invalid input! Try again")
