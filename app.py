import db, time


def menu():
    print("*"*40,"\n")
    print("\n🎯 Perfume Inventory App")
    print("1. Add new perfume")
    print("2. View all perfumes")
    print("3. Search by name")
    print("4. Update perfume (by name)")
    print("5. Delete perfume (by ID)")
    print("6. Exit\n")
    print("*"*40,"\n")

def main():
    db.connect()


    while True:
        menu()
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("\nEnter perfume name: ").lower()
            try:
                stock_input = input("Enter stock (leave blank for 0): ").strip()
                stock = int(stock_input) if stock_input else 0

                price = float(input("Enter price: "))
                db.add_perfume(name, stock, price)
                print("✅ Perfume added!")
            except ValueError:
                print("❌ Invalid stock or price. Try again.")

        elif choice == '2':
            perfumes = db.get_all_perfumes()
            if perfumes:
                for p in perfumes:
                    print(f"\n🧴 ID: {p[0]} | Name: {p[1]} | Stock: {p[2]} | Price: ₹{p[3]:.2f}/tola\n")
                    time.sleep(1)
                time.sleep(2)
            else:
                print("❌ No perfumes in inventory.")

        elif choice == '3':
            name = input("\nEnter name to search: ").lower()
            results = db.search_perfume(name)
            if results:
                for p in results:
                    print(f"\n🔍 ID: {p[0]} | Name: {p[1]} | Stock: {p[2]} | Price: ₹{p[3]:.2f}/tola\n")
                time.sleep(2)
            else:
                print("❌ No matching perfumes found.")

        elif choice == '4':
            name = input("\nEnter perfume name to update: ").lower()
            matches = db.search_perfume(name)

            if matches:
                print("🔍 Found these matching perfumes:")
                for p in matches:
                    print(f"\n🧴 ID: {p[0]} | Name: {p[1]} | Stock: {p[2]} | Price: ₹{p[3]:.2f}\n")


            try:
                id = int(input("\nEnter the ID of the perfume you want to update: "))
                stock_input = input("Enter stock (leave blank for 0): ").strip()
                stock = int(stock_input) if stock_input else 0

                price = float(input("Enter new price: "))
                db.update_perfume(id, stock, price)
                print("🔁 Perfume updated!")
            except ValueError:
                print("❌ Invalid input. Try again.")

        elif choice == '5':
            name = input("\nEnter perfume name to delete: ").lower()
            matches = db.search_perfume(name)

            if matches:
                print("🔍 Found these matching perfumes:")
                for p in matches:
                    print(f"\n🧴 ID: {p[0]} | Name: {p[1]} | Stock: {p[2]} | Price: ₹{p[3]:.2f}\n")

                try:
                    id_to_delete = int(input("Enter the ID of the perfume you want to delete: "))
                    confirm = input("Are you sure you want to delete this perfume? (y/n): ").lower()
                    if confirm == 'y':
                        db.delete_perfume_by_id(id_to_delete)
                        print("🗑️ Perfume deleted!")
                    else:
                        print("❎ Deletion cancelled.")
                except ValueError:
                    print("❌ Invalid ID entered.")
            else:
                print("❌ No matching perfumes found.")

        elif choice == '6':
            print("\n👋 Exiting. Bye!\n")
            break

        else:
            print("\n❌ Invalid choice. Enter a number from 1 to 6.\n")
            time.sleep(1.5)

if __name__ =='__main__':
    main()