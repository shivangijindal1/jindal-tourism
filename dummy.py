import tkinter as tk
from tkinter import messagebox  # Importing messagebox for popups
from tkinter import PhotoImage

# Simple cart list to store tour items
cart = []

# Free and Paid tour dictionaries with prices for paid tours
free_tours = {
    "Dubare Elephant Camp Tour": "Experience the beauty of nature and interact with elephants in their natural habitat.",
    "Abbey Falls Tour": "Visit the stunning Abbey Falls and enjoy a picturesque view of the surrounding hills.",
    "Namdroling Monastery Tour": "A spiritual haven."
    }

paid_tours = {
    "Coffee Plantation Tour": ("Explore the rich coffee plantations of Coorg.", 1000),  # price in Rs
    "Adventure Trekking Tour": ("Experience the thrill of trekking in Coorg's scenic landscapes.", 1500),
    "Wildlife Safari Tour": ("Get up close with Coorg's diverse wildlife.", 1200),
    "Raja's Seat Garden Tour": ("About 1 km west of the Madikeri bus stand is Raja’s Seat. Popular lore claims that Kodava kings their consorts spent their evenings in the fine park here. It is easy to see why: dramatic views of an orange sun dipping behind the mountains can mesmerize both royals and commoners. This point overlooks green mountains and valleys, beribboned with the distant silver of roads and rivers. \n\n Entry: Rs1500. ", 1500)
}

# New Transportation options dictionary
book_trans = {
    "Flight Booking": ("Book your flights with ease.", 3000),
    "Train Booking": ("Enjoy comfortable train travel.", 1500),
    "Bus Booking": ("Affordable bus travel options.", 800)
}

# Function to create a new window for tour information
def show_tour_info(tour_name, tour_info):
    info_window = tk.Toplevel(root)
    info_window.title(tour_name)
    info_window.geometry("1300x800")
    info_window.configure(bg="#C3B1E1")  # Set background color to light purple
    
    # Title label for the tour info window
    tour_title_label = tk.Label(info_window, text=tour_name, height=2, width=30, font=("Lucida Handwriting", 18, "bold"), bg="#C3B1E1", fg="brown")
    tour_title_label.pack(pady=10)

    # Tour information label
    tour_label = tk.Label(info_window, text=tour_info, wraplength=350, bg="#C3B1E1", font=("Arial", 12, "bold"))
    tour_label.pack(pady=20)

    # Button to add to cart
    add_button = tk.Button(info_window, text="Add to Cart", command=lambda: add_to_cart(tour_name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    add_button.pack(pady=10)

    # Close button
    close_button = tk.Button(info_window, text="Close", command=info_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to add tour to cart
def add_to_cart(tour_name):
    if tour_name not in cart:  # Prevent adding duplicates
        cart.append(tour_name)
    show_cart()  # Show the updated cart page

# Function to show the cart content and allow checkout
def show_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Cart")
    cart_window.geometry("1300x800")
    cart_window.configure(bg="#C3B1E1")  # Set cart window background color

    # Cart items label
    if cart:
        cart_items = "\n".join(cart)
        cart_label = tk.Label(cart_window, text=f"Items in your cart:\n{cart_items}", bg="#C3B1E1", font=("Arial", 14, "bold"))
        cart_label.pack(pady=20)
        
        checkout_button = tk.Button(cart_window, text="Checkout", command=show_checkout, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
        checkout_button.pack(pady=10)
    else:
        empty_cart_label = tk.Label(cart_window, text="Your cart is empty!", bg="#C3B1E1", font=("Arial", 14, "bold"))
        empty_cart_label.pack(pady=20)

    close_button = tk.Button(cart_window, text="Close", command=cart_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to show the checkout page
def show_checkout():
    checkout_window = tk.Toplevel(root)
    checkout_window.title("Checkout")
    checkout_window.geometry("1300x800")
    checkout_window.configure(bg="#C3B1E1")  # Set checkout window background color

    # Show selected tours
    checkout_label = tk.Label(checkout_window, text="You have selected the following tours and transportation:", 
                               font=("Arial", 14, "bold"), bg="#C3B1E1")
    checkout_label.pack(pady=10)

    total_amount = 0  # Initialize total amount
    for tour in cart:
        if tour in free_tours:
            # If it's a free tour, no cost
            tour_price = 0
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Free)", font=("Arial", 12), bg="#C3B1E1")
        elif tour in paid_tours:
            # If it's a paid tour, get the price
            tour_price = paid_tours[tour][1]  # Get the price of the paid tour
            total_amount += tour_price
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Paid: Rs {tour_price})", font=("Arial", 12), bg="#C3B1E1")
        elif tour in book_trans:
            # If it's transportation, get the price
            tour_price = book_trans[tour][1]  # Get the price of the transportation
            total_amount += tour_price
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Transport: Rs {tour_price})", font=("Arial", 12), bg="#C3B1E1")
        
        tour_label.pack()

    total_label = tk.Label(checkout_window, text=f"Total Amount to be Paid: Rs {total_amount}", 
                            font=("Arial", 14, "bold"), bg="#C3B1E1")
    total_label.pack(pady=10)

    donation_label = tk.Label(checkout_window, text="Would you like to make a donation? ", bg="#C3B1E1", font=("Arial", 12, "bold"))
    donation_label.pack(pady=5)

    donation_entry = tk.Entry(checkout_window)
    donation_entry.pack(pady=5)

    # Confirm booking button
    confirm_button = tk.Button(checkout_window, text="Confirm Booking", command=lambda: confirm_booking(donation_entry.get(), total_amount), 
                                height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    confirm_button.pack(pady=10)

    # Close button
    close_button = tk.Button(checkout_window, text="Close", command=checkout_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to confirm the booking and show confirmation page
def confirm_booking(donation, total_amount):
    booking_details = "\n".join(cart)  # Get the booked tours
    show_confirmation_page(booking_details, donation, total_amount)

# Function to show the booking confirmation page
def show_confirmation_page(booking_details, donation, total_amount):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Booking Confirmation")
    confirmation_window.geometry("1300x800")
    confirmation_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    confirmation_label = tk.Label(confirmation_window, text="Booking Confirmation", font=("Lucida Handwriting", 24, "bold"), bg="#C3B1E1", fg="brown")
    confirmation_label.pack(pady=10)

    if donation and donation.isdigit():
        donation_amount = int(donation)
        thank_you_message = f"Thank you for your generous donation of Rs {donation_amount}!\n"
    else:
        donation_amount = 0
        thank_you_message = "Thank you!\n"

    details_label = tk.Label(confirmation_window, text=f"{thank_you_message}Details of your booking:\n{booking_details}\nTotal Amount: Rs {total_amount} + {donation_amount}", 
                              wraplength=350, bg="#C3B1E1", font=("Arial", 14, "bold"))
    details_label.pack(pady=20)

    pay_button = tk.Button(confirmation_window, text="Pay Now", command=lambda: confirm_payment(total_amount, donation_amount), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    pay_button.pack(pady=10)

    close_button = tk.Button(confirmation_window, text="Close", command=confirmation_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to handle payment confirmation
def confirm_payment(total_amount, donation_amount):
    messagebox.showinfo("Payment Confirmation", f"Payment of Rs {total_amount + donation_amount} confirmed! Thank you for booking with us!")
    cart.clear()  # Clear the cart after payment
    root.quit()  # Exit the application after payment confirmation

# Function to book transportation
def book_transportation():
    trans_window = tk.Toplevel(root)
    trans_window.title("Book Transportation")
    trans_window.geometry("1300x800")
    trans_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    trans_label = tk.Label(trans_window, text="Choose a mode of transportation:", font=("Lucida Handwriting", 18, "bold"), bg="#C3B1E1", fg="brown")
    trans_label.pack(pady=10)

    # Create buttons for each transportation option
    for trans_name, (trans_info, price) in book_trans.items():
        trans_button = tk.Button(trans_window, text=trans_name, command=lambda name=trans_name: show_trans_info(name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
        trans_button.pack(pady=5)

    view_cart_button = tk.Button(trans_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)

    back_button = tk.Button(trans_window, text="Back to Home", command=trans_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    back_button.pack(pady=5)

# Function to show transportation information
def show_trans_info(trans_name):
    trans_info = book_trans[trans_name][0]
    trans_window = tk.Toplevel(root)
    trans_window.title(trans_name)
    trans_window.geometry("1300x800")
    trans_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    # Title label for the transportation info window
    trans_title_label = tk.Label(trans_window, text=trans_name, font=("Lucida Handwriting", 18, "bold"), bg="#C3B1E1", fg="brown")
    trans_title_label.pack(pady=10)

    # Transportation information label
    trans_label = tk.Label(trans_window, text=trans_info, wraplength=350, bg="#C3B1E1", font=("Arial", 12, "bold"))
    trans_label.pack(pady=20)

    # Add to cart button
    add_to_cart_button = tk.Button(trans_window, text="Add to Cart", command=lambda: add_to_cart(trans_name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    add_to_cart_button.pack(pady=10)

    close_button = tk.Button(trans_window, text="Close", command=trans_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to show free tours
def show_free_tours():
    free_tours_window = tk.Toplevel(root)
    free_tours_window.title("Free Tours")
    free_tours_window.geometry("1300x800")
    free_tours_window.configure(bg="#C3B1E1")  # Set background color to light purple

    # Title label for free tours window
    free_tours_label = tk.Label(free_tours_window, text="Available Free Tours", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    free_tours_label.pack(pady=10)

    free_tours_label = tk.Label(free_tours_window, text="\n \n We offer a range of free of cost tours as an initiative to promote tourism in Coorg! \n \n ", font=("Arial", 16, "bold"), bg="pink", fg="black")
    free_tours_label.pack(pady=10)
    # Create buttons for each free tour
    for tour_name, tour_info in free_tours.items():
        tour_button = tk.Button(free_tours_window, text=tour_name, 
                                command=lambda name=tour_name, info=tour_info: show_tour_info(name, info), 
                                height=2, width=30, font=("Arial", 14, "bold"), bg="#FFD700")
        tour_button.pack(pady=10)

    close_button = tk.Button(free_tours_window, text="Close", command=free_tours_window.destroy, 
                             height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)
    close_button.place(x=20,y=550)
    back_button = tk.Button(free_tours_window, text="Back to Home", command=free_tours_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)
# Function to show paid tours
def show_paid_tours():
    paid_tours_window = tk.Toplevel(root)
    paid_tours_window.title("Paid Tours")
    paid_tours_window.geometry("1300x800")
    paid_tours_window.configure(bg="#C3B1E1")  # Set background color to light purple

    # Title label for paid tours window
    paid_tours_label = tk.Label(paid_tours_window, text="Available Paid Tours", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    paid_tours_label.pack(pady=10)

    paid_tours_label = tk.Label(paid_tours_window, text="We provide some extraordinary tours at a very low cost as well! \n Happy travels!", font=("Arial", 14, "bold"), bg="pink", fg="black")
    paid_tours_label.pack(pady=10)

    # Create buttons for each paid tour
    for tour_name, (tour_info, price) in paid_tours.items():
        tour_button = tk.Button(paid_tours_window, text=tour_name, 
                                command=lambda name=tour_name, info=tour_info: show_tour_info(name, info), 
                                height=2, width=30, font=("Arial", 14, "bold"), bg="#FFD700")
        tour_button.pack(pady=10)

    close_button = tk.Button(paid_tours_window, text="Close", command=paid_tours_window.destroy, 
                             height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Main application window
root = tk.Tk()
root.title("JindalTourism.net")
root.geometry("1300x800")  # Set window size
root.configure(bg="#C3B1E1")  # Set background color to light purple

# Load an image for the home page (make sure to provide a valid path to your image)
# image = PhotoImage(file="path/to/your/image.png")
# image_label = tk.Label(root, image=image, bg="#C3B1E1")
# image_label.pack(pady=10)
image_path=PhotoImage(file=r"C:\Users\Shivangi\Desktop\logo.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

# Title label
title_label = tk.Label(root, text="Welcome to Jindal Tourism!", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
title_label.pack(pady=10)

# Introduction label
intro_label = tk.Label(root, text="Book tours and transport at the click of a button!!", bg="#C3B1E1", font=("Arial", 18, "bold"))
intro_label.pack(pady=5)

# Introduction label
intro_label = tk.Label(root, text="Jindal Tourism aims at bringing you tours and travels to the hidden gems of Coorg!  \n\n", bg="#C3B1E1", font=("Arial", 14, "bold"))
intro_label.pack(pady=5)

# Button to show free tours
free_tours_button = tk.Button(root, text="Free Tours", command=show_free_tours, height=2, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
free_tours_button.pack(pady=5)

# Button to show paid tours
paid_tours_button = tk.Button(root, text="Paid Tours", command=show_paid_tours, height=2, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
paid_tours_button.pack(pady=5)

# Button to book transport
book_transport_button = tk.Button(root, text="Book Transportation", command=book_transportation, height=2, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
book_transport_button.pack(pady=5)

# Button to view cart
view_cart_button = tk.Button(root, text="View Cart", command=show_cart, height=2, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
view_cart_button.pack(pady=5)

# Introduction label
intro_label = tk.Label(root, text="THIS MONTH'S HIDDEN GEM IS: ", bg="#C3B1E1", font=("Lucida Handwriting", 24, "bold", "underline"))
intro_label.pack(pady=5)

# Title label
title_label = tk.Label(root, text="ABBEY FALLS", font=("Lucida Handwriting", 28, "bold"), bg="#C3B1E1", fg="brown")
title_label.pack(pady=10)

# Button to go to 'About Us'
about_us_button = tk.Button(root, text="About Us", command=lambda: show_about_us(), height=2, width=40, font=("Arial", 14, "bold"), bg="Pink")
about_us_button.pack(pady=10)


# Function to show About Us information
def show_about_us():
    about_us_window = tk.Toplevel(root)
    about_us_window.title("About Us")
    about_us_window.geometry("1300x800")
    about_us_window.configure(bg="#C3B1E1")  # Set background color to light purple
    
    about_label = tk.Label(about_us_window, text="About Us", font=("Lucida Handwriting", 24, "bold"), bg="#C3B1E1", fg="brown")
    about_label.pack(pady=10)

    about_text = "Welcome to Jindal Tourism, your premier destination for exploring the enchanting beauty of Coorg! Our mission is to provide unforgettable experiences that showcase the hidden gems of this lush region while making tourism accessible to all. \n \n At Jindal Tourism, we believe that everyone deserves the opportunity to explore  the breathtaking landscapes and rich cultural heritage of Coorg. That’s why we proudly offer a variety of free tours designed to encourage tourism and allow visitors to immerse themselves in the natural splendor of the area. \n \n In addition to our free tours, we offer a selection of paid tours that cater to diverse interests, from adventure seekers to cultural enthusiasts. Each tour is crafted with care, ensuring that every guest has a memorable and enriching experience. \n \n To complement our tour offerings, we also provide affordable travel tickets at fixed rates, making it easy for you to explore Coorg without breaking the bank. Whether you're planning a weekend getaway or a week-long adventure,  Jindal Tourism is here to help you make the most of your travels. \n \n Join us as we embark on a journey to discover the magic of Coorg.  We look forward to welcoming you!"
    about_info_label = tk.Label(about_us_window, text=about_text, wraplength=800, bg="#C3B1E1", font=("Arial", 14))
    about_info_label.pack(pady=20)

    close_button = tk.Button(about_us_window, text="Close", command=about_us_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Run the application
root.mainloop()

