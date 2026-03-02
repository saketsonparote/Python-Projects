import streamlit as st
import json
import random
import string
from pathlib import Path
from datetime import datetime

class Library:

    database = "library.json"
    data = {"books": [], "members": []}

    # Load data
    if Path(database).exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def gen_id(prefix="B"):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return f"{prefix}-{random_id}"

    @classmethod
    def save_data(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4, default=str)

lib = Library()

st.title("📚 Library Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Book", "List Books", "Add Member", "List Members", "Borrow Book", "Return Book"]
)

# ---------------- ADD BOOK ----------------
if menu == "Add Book":
    st.subheader("Add New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author")
    copies = st.number_input("Total Copies", min_value=1, step=1)

    if st.button("Add Book"):
        book = {
            "id": Library.gen_id(),
            "title": title,
            "author": author,
            "total_copies": copies,
            "available_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Library.data["books"].append(book)
        Library.save_data()
        st.success("Book Added Successfully!")

# ---------------- LIST BOOKS ----------------
elif menu == "List Books":
    st.subheader("All Books")

    if not Library.data["books"]:
        st.warning("No books available")
    else:
        st.table(Library.data["books"])

# ---------------- ADD MEMBER ----------------
elif menu == "Add Member":
    st.subheader("Add New Member")

    name = st.text_input("Member Name")
    email = st.text_input("Email")

    if st.button("Add Member"):
        member = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed": []
        }

        Library.data["members"].append(member)
        Library.save_data()
        st.success("Member Added Successfully!")

# ---------------- LIST MEMBERS ----------------
elif menu == "List Members":
    st.subheader("All Members")

    if not Library.data["members"]:
        st.warning("No members found")
    else:
        st.table(Library.data["members"])

# ---------------- BORROW BOOK ----------------
elif menu == "Borrow Book":
    st.subheader("Borrow Book")

    member_ids = [m["id"] for m in Library.data["members"]]
    book_ids = [b["id"] for b in Library.data["books"] if b["available_copies"] > 0]

    member_id = st.selectbox("Select Member", member_ids)
    book_id = st.selectbox("Select Book", book_ids)

    if st.button("Borrow"):
        member = next((m for m in Library.data["members"] if m["id"] == member_id), None)
        book = next((b for b in Library.data["books"] if b["id"] == book_id), None)

        if member and book:
            borrow_entry = {
                "book_id": book["id"],
                "title": book["title"],
                "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            member["borrowed"].append(borrow_entry)
            book["available_copies"] -= 1
            Library.save_data()
            st.success("Book Borrowed Successfully!")

# ---------------- RETURN BOOK ----------------
elif menu == "Return Book":
    st.subheader("Return Book")

    member_ids = [m["id"] for m in Library.data["members"]]
    member_id = st.selectbox("Select Member", member_ids)

    member = next((m for m in Library.data["members"] if m["id"] == member_id), None)

    if member and member["borrowed"]:
        borrowed_books = [f"{b['title']} ({b['book_id']})" for b in member["borrowed"]]
        selected = st.selectbox("Select Book to Return", borrowed_books)

        if st.button("Return Book"):
            index = borrowed_books.index(selected)
            returned = member["borrowed"].pop(index)

            book = next((b for b in Library.data["books"] if b["id"] == returned["book_id"]), None)
            if book:
                book["available_copies"] += 1

            Library.save_data()
            st.success("Book Returned Successfully!")
    else:
        st.warning("No borrowed books for this member.")