from customtkinter import CTk, CTkLabel, CTkButton, CTkTabview

def open_menu_window():
    menu_window = CTk()
    menu_window.title("Menu")
    menu_window.geometry("700x500")

    # Create a tabview widget
    tabview = CTkTabview(menu_window)
    tabview.pack(fill="both", expand=True)

    # Add tabs to the tabview
    tab_1 = tabview.add("Chirstmas")
    tab_2 = tabview.add("Marvel")
    tab_3 = tabview.add("DC")

    btn = CTkButton(tab_1, text="Santa Clause")
    btn.pack(pady=20)
    
    btn2 = CTkButton(tab_1, text="Jack Frost")
    btn2.pack(pady=20)
    
    btn3 = CTkButton(tab_1, text="Rudolph")
    btn3.pack(pady=20)
    #Marvel
    btn = CTkButton(tab_2, text="Hulk")
    btn.pack(pady=20)
    
    btn2 = CTkButton(tab_2, text="Iron Man")
    btn2.pack(pady=20)
    
    btn3 = CTkButton(tab_2, text="Spider-Man")
    btn3.pack(pady=20)
    #DC
    btn = CTkButton(tab_3, text="Batman")
    btn.pack(pady=20)
    
    btn2 = CTkButton(tab_3, text="Aquaman")
    btn2.pack(pady=20)
    
    btn3 = CTkButton(tab_3, text="Superman")
    btn3.pack(pady=20)

    menu_window.mainloop()
