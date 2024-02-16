import random
import tkinter as tk
from tkinter import simpledialog, messagebox

class CoffeeGroup:
    def __init__(self):
        self.coworkers = {}  # List of all the coworkers
        self.menu = {
            'Black': 2.0,
            'Espresso': 2.5,
            'Latte': 3.5,
            'Americano': 2.75,
            'Cappuccino': 3.5,
            'Mocha': 4.0,
            'Cafe Au Lait': 3.0,
            'Macchiato': 3.0,
            'Caramel Macchiato': 3.75,
            'Flat White': 3.75,
            'Irish Coffee': 5.0,
            'Frappe': 4.5,
            'Cold Brew': 3.5,
            'Affogato': 4.5,
            'Red Eye': 3.25,
            'Vietnamese Coffee': 4.0
        }  # Menu

    def add_coworker(self, name, favorite_coffee): # Before anyone paid for any coffee we add coworker
        if name in self.coworkers: # Checking if name is in the system
            print(f"{name} is already in the system.")
            return
        if favorite_coffee not in self.menu: # Checking if coffee is valid
            print(f"{favorite_coffee} is not in the menu. Please press the menu button for reference.")
            return

        self.coworkers[name] = { # Configuring architect for coworker's attributes
            'favorite_coffee': favorite_coffee,
            'total_paid': 0,
            'average_cost': self.menu[favorite_coffee],
            'counter':0
        }

    def update_payment(self, name, amount): # updates payment after paying for the coffees
        if name in self.coworkers:
            self.coworkers[name]['total_paid'] += amount
        else:
            print(f"{name} not found in the system.")

    def next_to_pay(self): # Algorithm to figure out who is paying next. Figures out the ratio between the total paid and the average cost of the coffee.
        min_paid_ratio = float('inf')
        next_payer = None
        for name, info in self.coworkers.items():
            paid_ratio = info['total_paid'] / info['average_cost']
            if paid_ratio < min_paid_ratio:
                min_paid_ratio = paid_ratio
                next_payer = name
        return next_payer

    def add_new_coworker(self, name, favorite_coffee): # After someone paid for the coffee and wants to add new coworker.
        if len(self.coworkers) > 0:
            average_total_paid = sum(info['total_paid'] for info in self.coworkers.values()) / len(self.coworkers)
        else:
            average_total_paid = 0  # If there are no coworkers yet, start at 0

        self.coworkers[name] = {
            'favorite_coffee': favorite_coffee,
            'total_paid': average_total_paid,
            'average_cost': self.menu.get(favorite_coffee, 0)  # Default to 0 if coffee not found
        }

    def change_coffee_preference(self, name, new_favorite_coffee): # Change the coffee preference
        self.coworkers[name]['favorite_coffee'] = new_favorite_coffee
        self.coworkers[name]['average_cost'] = self.menu[new_favorite_coffee]
        
        

    def delete_coworker(self, name): # Deleting coworker from the system
        if name not in self.coworkers:
            print(f"{name} not found in the system.")
            return

        # Removing the coworker from the group
        del self.coworkers[name]

        # Recalculating and adjust payments among the remaining coworkers
        if len(self.coworkers) > 0:
            average_total_paid = sum(info['total_paid'] for info in self.coworkers.values()) / len(self.coworkers)
            for info in self.coworkers.values():
                info['total_paid'] = average_total_paid
        else:
            messagebox.showinfo("No coworkers left in the system.")

    def random_coworker_to_pay(self): # Random coworker feature
        if not self.coworkers:
            return None
        
        random_name = random.choice(list(self.coworkers.keys()))
        return random_name
    




class CoffeeGroupUI: # GUI class
    def __init__(self, master):
        self.master = master
        master.title("JavaTurn")

        self.coffee_group = CoffeeGroup() # Using Class from above

        self.top_frame = tk.Frame(master) # Creating a frame for the title and menu button
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.top_frame, text="JavaTurn", font=("Arial", 24)) # Creating and centering the title label within the frame
        self.title_label.pack(side=tk.LEFT, expand=True, padx=(80,0), pady = (5,0))

        self.menu_button = tk.Button(self.top_frame, text="Menu", command=self.show_menu) # Creating and place the menu button to the right within the frame
        self.menu_button.pack(side=tk.RIGHT, padx=(0,10),pady=(5,0))

        self.display_area = tk.Text(master, height=15, width=70)  # Display Area for Coworkers
        self.display_area.pack(padx=5, pady=5)

        self.top_button_frame = tk.Frame(master) # Creating two frames for the button groups: one for the left side and one for the right side
        self.left_button_frame = tk.Frame(master)
        self.right_button_frame = tk.Frame(master)

        self.top_button_frame.pack(side=tk.TOP, fill=tk.Y, padx=(0,0), pady=0) # Packing the frames to the left, right, and top of the display area 
        self.left_button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(120,2), pady=(0,10))  # Fillin in the Y direction to align vertically
        self.right_button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(2,120), pady=(0,10))  # Filling in the Y direction to align vertically

        self.update_preference_button = tk.Button(self.top_button_frame, text="Update Preference", command=self.update_coffee_preference_ui) # Preference button in Top Frame
        self.update_preference_button.pack(pady=0,padx=(0,10))

        self.add_coworker_button = tk.Button(self.left_button_frame, text="Add Coworker", command=self.add_coworker) # Adding Add Coworker and Next Pay buttons to the left frame for vertical alignment
        self.next_pay_button = tk.Button(self.left_button_frame, text="Next Pay", command=self.next_to_pay)
        self.add_coworker_button.pack(pady=5) 
        self.next_pay_button.pack(pady=5, padx=(30,0))
        
        self.delete_coworker_button = tk.Button(self.right_button_frame, text="Delete Coworker", command=self.delete_coworker_ui) #Adding "Delete Coworker" and "Random" buttons to the right frame for vertical alignment
        self.random_button = tk.Button(self.right_button_frame, text="Random", command=self.random_coworker_to_pay)
        self.delete_coworker_button.pack(pady=5)  # Add some vertical padding between buttons
        self.random_button.pack(pady=5,padx=(0,50))
        
        self.update_display() # Updating Display 

    def show_menu(self):
        menu_window = tk.Toplevel(self.master) # Creating a new window for the menu
        menu_window.title("Coffee Menu")
        
        for coffee, cost in self.coffee_group.menu.items(): # Displaying each coffee and its cost
            tk.Label(menu_window, text=f"{coffee}: ${cost}").pack(anchor=tk.W)

    def add_coworker(self): 
        name = simpledialog.askstring("Name", "Name of the coworker:", parent=self.master)
        if name is None:  # Explicitly check if Cancel was pressed
            return  # Exiting the function early

        favorite_coffee = simpledialog.askstring("Coffee", "Favorite coffee:", parent=self.master)
        if favorite_coffee is None or favorite_coffee not in self.coffee_group.menu:  # Again, check if Cancel was pressed
            messagebox.showinfo('Error', f"{favorite_coffee} is not in the menu. Please press the menu button for reference.")
            return 

        self.coffee_group.add_coworker(name, favorite_coffee)
        self.update_display()


    def next_to_pay(self):
        next_payer = self.coffee_group.next_to_pay()
        if not next_payer:
            messagebox.showinfo("Next to Pay", "No one is in the queue to pay.")
            return

        self.next_pay_window = tk.Toplevel(self.master)
        self.next_pay_window.title("Next to Pay")
        self.next_pay_window.geometry("200x100")

        tk.Label(self.next_pay_window, text=f"{next_payer} ", font=('Helvetica', 18, 'bold')).pack()
        tk.Label(self.next_pay_window, text="is next to pay.", font=('Helvetica')).pack()

        tk.Button(self.next_pay_window, text="Paid", command=self.coworker_paid).pack(pady=(10,0)) # Call coworker_paid directly with a fixed or calculated payment amount



    def random_coworker_to_pay(self):
        selected = self.coffee_group.random_coworker_to_pay()  # This call gets the selected coworker's name
        if selected:
            # Directly use the returned value in the messagebox
            messagebox.showinfo("Random Pay", f"{selected} has been randomly selected to pay.")
        else:
            messagebox.showerror("Error", "No coworkers in the system.")

    def coworker_paid(self):
        next_payer = self.coffee_group.next_to_pay()
        if not next_payer:
            messagebox.showinfo("Info", "No next payer found.")
            return
        
        # Calculate the total payment amount as the summation of all the preferred coffee costs
        payment_amount = sum(self.coffee_group.menu[info['favorite_coffee']] for info in self.coffee_group.coworkers.values())
        
        self.coffee_group.update_payment(next_payer, payment_amount)
        self.update_display()
        self.next_pay_window.destroy() 
        
    def update_coffee_preference_ui(self):
        name = simpledialog.askstring("Update Preference", "Enter the coworker's name:", parent=self.master)
        if not name or name not in self.coffee_group.coworkers:
            messagebox.showerror("Error", "Coworker not found.")
            return

        new_favorite_coffee = simpledialog.askstring("Update Preference", "Enter the new favorite coffee:", parent=self.master)
        if not new_favorite_coffee or new_favorite_coffee not in self.coffee_group.menu:
            messagebox.showerror("Error", f"{new_favorite_coffee} is not in the menu. Please check the menu for available options.")
            return

        self.coffee_group.change_coffee_preference(name, new_favorite_coffee)
        self.update_display()
        messagebox.showinfo("Updated", f"{name}'s favorite coffee has been updated to {new_favorite_coffee}.")

    def update_display(self):
        self.display_area.delete(1.0, tk.END)
        total_paid = sum(info['total_paid'] for info in self.coffee_group.coworkers.values())
        if total_paid > 0 and self.add_coworker_button['text'] != "Add New Coworker":
            self.add_coworker_button.config(text="Add New Coworker", command=self.add_new_coworker)
        
        for name, info in self.coffee_group.coworkers.items():
            paid_ratio = info['total_paid'] / info['average_cost'] if info['average_cost'] else 0
            self.display_area.insert(tk.END, f"{name}: {info['favorite_coffee']} - Cost: ${info['average_cost']} - Paid: ${info['total_paid']} - Ratio: {paid_ratio:.2f}\n")
        

    def add_new_coworker(self): # Function to add a new coworker after someone has paid
        name = simpledialog.askstring("Input", "Name of the new coworker:", parent=self.master)
        favorite_coffee = simpledialog.askstring("Input", "Favorite coffee:", parent=self.master)
        if name and favorite_coffee:
            self.coffee_group.add_new_coworker(name, favorite_coffee)
            self.update_display()


    def delete_coworker_ui(self):
        name = simpledialog.askstring("Delete Coworker", "Enter coworker's name to delete:", parent=self.master)
        if not name or name not in self.coffee_group.coworkers:
            messagebox.showerror("Error", "Coworker not found or no name entered.")
            return
        
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?", icon='warning')
        if confirm:
            self.coffee_group.delete_coworker(name)
            messagebox.showinfo("Deleted", f"{name} has been deleted.")
            self.update_display()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeGroupUI(root)
    root.mainloop()
