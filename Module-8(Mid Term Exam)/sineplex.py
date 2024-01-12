class Hall:
    seats = {}
    showlist = []
    seatRep = []
    def __init__(self, rows, cols, hall_no) -> None:
        
        self.rows = rows
        self.comums = cols
        self.hall_no = hall_no
        
    
    def entry_show(self, id, movie_name, time):
        tp = (id, movie_name, time)
        self.showlist.append(tp)
        for _ in range(self.rows):
            seats_in_line = []
            for _ in range(self.comums):
                seats_in_line.append(0)
            self.seatRep.append(seats_in_line)
        self.seats[id] = self.seatRep
    
    def book_seats(self, id, list_tup):
        for key in self.seats:
            if key == id:
                self.seatRep[list_tup[0]][list_tup[1]] = 1
                return
            else:
                print("No Show is running with this name Today")
    
    def view_show_list(self):
        for show in self.showlist:
            print(show)

    def view_available_seats(self, id):
        for key in self.seats:
            if key == id:
                # print(self.seats[id])
                for ele in self.seats[id]:
                    print(ele)
                return
            else:
                print("Now show in this name")
    
class StartCinema:
    hall_list = []
    hall_list_name = []
    def entry_hall(self, hallObj):
        self.hall_list.append(hallObj)
    def __repr__(self) -> str:
        return self.hall_list
    
sena = Hall(5, 5, 0)
savar = StartCinema()
savar.entry_hall(sena)
print(StartCinema)
# sena.entry_show('1065', "Jawan", "12/01/24 10 : 00 PM")
# sena.entry_show('1055', "Pathan", "12/01/24 01 : 00 AM")
# sena.book_seats('1065', (4, 4))
# sena.view_available_seats('1065')



# while True:
#     print("1. VIEW ALL SHOW TODAY")
#     print("2. VIEW AVAILABLE SEATS")
#     print("3. BOOK TICKET")
#     print("4. EXIT")
    
#     op = int(input("Enter Option: "))
    
#     if op == 1:
#         print("OP- 1")
#     elif op == 2:
#         print("OP-2")
#     elif op == 3:
#         print("OP-3")
#     elif op == 4:
#         print("Exited")
#         break
#     else:
#         print("Wrong choice, Enter again")