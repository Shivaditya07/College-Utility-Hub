import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import random

class CollegeUtilityHub:
    def __init__(self, root):
        self.root = root
        self.root.title("University Utility Hub - Student Services Portal")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a1a")
        
        # Color scheme - Dark Greyish Professional Theme
        self.colors = {
            'bg_dark': '#1a1a1a',
            'bg_medium': '#2d2d2d',
            'bg_light': '#3d3d3d',
            'accent': '#4a90e2',
            'accent_hover': '#5ba3ff',
            'text_primary': '#e0e0e0',
            'text_secondary': '#a0a0a0',
            'success': '#4caf50',
            'warning': '#ff9800',
            'error': '#f44336'
        }
        
        # Student data (simulated)
        self.student_id = "STU" + str(random.randint(100000, 999999))
        self.student_name = "John Anderson"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header Section
        header_frame = tk.Frame(self.root, bg=self.colors['bg_medium'], height=80)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # University Logo/Name
        title_label = tk.Label(
            header_frame,
            text="🎓 UNIVERSITY UTILITY HUB",
            font=("Helvetica", 24, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['accent']
        )
        title_label.pack(side='left', padx=30, pady=20)
        
        # Student Info
        info_frame = tk.Frame(header_frame, bg=self.colors['bg_medium'])
        info_frame.pack(side='right', padx=30)
        
        student_label = tk.Label(
            info_frame,
            text=f"Student: {self.student_name}",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        student_label.pack(anchor='e')
        
        id_label = tk.Label(
            info_frame,
            text=f"ID: {self.student_id}",
            font=("Helvetica", 9),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_secondary']
        )
        id_label.pack(anchor='e')
        
        # Main Container
        main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left Panel - Service Categories
        left_panel = tk.Frame(main_container, bg=self.colors['bg_medium'], width=350)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)
        
        services_title = tk.Label(
            left_panel,
            text="Administrative & Student Services",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        services_title.pack(pady=20, padx=15)
        
        # Service Buttons
        services = [
            ("💳 Fee Payment", self.open_fee_payment),
            ("🆔 ID Card Services", self.open_id_card),
            ("📜 Document Collection", self.open_documents),
            ("📚 Course Registration", self.open_course_registration),
            ("💰 Scholarship & Financial Aid", self.open_scholarship)
        ]
        
        for service_name, command in services:
            btn = tk.Button(
                left_panel,
                text=service_name,
                font=("Helvetica", 11),
                bg=self.colors['bg_light'],
                fg=self.colors['text_primary'],
                activebackground=self.colors['accent'],
                activeforeground='white',
                relief='flat',
                cursor='hand2',
                command=command,
                height=2,
                anchor='w',
                padx=20
            )
            btn.pack(fill='x', padx=15, pady=5)
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.colors['accent']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg=self.colors['bg_light']))
        
        # Right Panel - Content Area
        self.right_panel = tk.Frame(main_container, bg=self.colors['bg_medium'])
        self.right_panel.pack(side='right', fill='both', expand=True)
        
        # Welcome Screen
        self.show_welcome()
        
        # Footer
        footer = tk.Label(
            self.root,
            text=f"© 2026 University Portal | Last Login: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
            font=("Helvetica", 9),
            bg=self.colors['bg_dark'],
            fg=self.colors['text_secondary']
        )
        footer.pack(side='bottom', pady=10)
    
    def clear_panel(self):
        for widget in self.right_panel.winfo_children():
            widget.destroy()
    
    def show_welcome(self):
        self.clear_panel()
        
        welcome_label = tk.Label(
            self.right_panel,
            text=f"Welcome, {self.student_name}!",
            font=("Helvetica", 20, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        welcome_label.pack(pady=(50, 20))
        
        info_label = tk.Label(
            self.right_panel,
            text="Select a service from the menu to get started",
            font=("Helvetica", 12),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_secondary']
        )
        info_label.pack()
        
        # Quick Stats
        stats_frame = tk.Frame(self.right_panel, bg=self.colors['bg_medium'])
        stats_frame.pack(pady=40)
        
        stats = [
            ("Pending Fees", "$0", self.colors['success']),
            ("Enrolled Courses", "6", self.colors['accent']),
            ("Pending Documents", "0", self.colors['warning'])
        ]
        
        for title, value, color in stats:
            stat_box = tk.Frame(stats_frame, bg=self.colors['bg_light'], width=180, height=100)
            stat_box.pack(side='left', padx=15)
            stat_box.pack_propagate(False)
            
            tk.Label(
                stat_box,
                text=value,
                font=("Helvetica", 24, "bold"),
                bg=self.colors['bg_light'],
                fg=color
            ).pack(pady=(15, 5))
            
            tk.Label(
                stat_box,
                text=title,
                font=("Helvetica", 10),
                bg=self.colors['bg_light'],
                fg=self.colors['text_secondary']
            ).pack()
    
    def open_fee_payment(self):
        self.clear_panel()
        
        title = tk.Label(
            self.right_panel,
            text="💳 Fee Payment Portal",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        title.pack(pady=20)
        
        # Fee Categories
        fee_frame = tk.Frame(self.right_panel, bg=self.colors['bg_medium'])
        fee_frame.pack(pady=20, fill='both', expand=True, padx=40)
        
        fees = [
            ("Tuition Fee - Spring 2026", "$8,500"),
            ("Hostel Fee - Semester", "$2,200"),
            ("Library Fee", "$150"),
            ("Laboratory Fee", "$300"),
            ("Sports & Recreation", "$100")
        ]
        
        tk.Label(
            fee_frame,
            text="Select Fee Category:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 15))
        
        self.selected_fee = tk.StringVar(value=fees[0][0])
        
        for fee_name, amount in fees:
            rb_frame = tk.Frame(fee_frame, bg=self.colors['bg_medium'])
            rb_frame.pack(anchor='w', pady=5)
            
            tk.Radiobutton(
                rb_frame,
                text=fee_name,
                variable=self.selected_fee,
                value=fee_name,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(side='left')
            
            tk.Label(
                rb_frame,
                text=f"  ({amount})",
                font=("Helvetica", 11, "bold"),
                bg=self.colors['bg_medium'],
                fg=self.colors['accent']
            ).pack(side='left')
        
        # Payment Method
        payment_frame = tk.Frame(fee_frame, bg=self.colors['bg_medium'])
        payment_frame.pack(anchor='w', pady=20)
        
        tk.Label(
            payment_frame,
            text="Payment Method:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 10))
        
        self.payment_method = tk.StringVar(value="Credit/Debit Card")
        
        for method in ["Credit/Debit Card", "Bank Transfer", "UPI", "Campus Wallet"]:
            tk.Radiobutton(
                payment_frame,
                text=method,
                variable=self.payment_method,
                value=method,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(anchor='w', pady=3)
        
        # Pay Button
        pay_btn = tk.Button(
            self.right_panel,
            text="Proceed to Payment",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg='white',
            activebackground=self.colors['accent_hover'],
            relief='flat',
            cursor='hand2',
            command=self.process_payment,
            padx=30,
            pady=12
        )
        pay_btn.pack(pady=20)
    
    def process_payment(self):
        transaction_id = "TXN" + str(random.randint(100000, 999999))
        message = f"✓ Payment Processed Successfully!\n\n"
        message += f"Transaction ID: {transaction_id}\n"
        message += f"Fee Category: {self.selected_fee.get()}\n"
        message += f"Payment Method: {self.payment_method.get()}\n"
        message += f"Status: Completed\n\n"
        message += "Receipt has been sent to your registered email address."
        
        messagebox.showinfo("Payment Confirmation", message)
    
    def open_id_card(self):
        self.clear_panel()
        
        title = tk.Label(
            self.right_panel,
            text="🆔 ID Card Services",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        title.pack(pady=20)
        
        # Service Type
        service_frame = tk.Frame(self.right_panel, bg=self.colors['bg_medium'])
        service_frame.pack(pady=20, fill='both', expand=True, padx=40)
        
        tk.Label(
            service_frame,
            text="Select Service Type:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 15))
        
        self.id_service = tk.StringVar(value="New ID Card")
        
        services = [
            "New ID Card",
            "Lost ID Card Replacement",
            "Damaged ID Card Replacement",
            "ID Card Renewal",
            "Temporary ID Card"
        ]
        
        for service in services:
            tk.Radiobutton(
                service_frame,
                text=service,
                variable=self.id_service,
                value=service,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(anchor='w', pady=5)
        
        # Reason
        tk.Label(
            service_frame,
            text="Reason for Request:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(20, 10))
        
        self.id_reason = scrolledtext.ScrolledText(
            service_frame,
            height=3,
            width=60,
            font=("Helvetica", 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary']
        )
        self.id_reason.pack(anchor='w')
        
        # Submit Button
        submit_btn = tk.Button(
            self.right_panel,
            text="Submit Request",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg='white',
            activebackground=self.colors['accent_hover'],
            relief='flat',
            cursor='hand2',
            command=self.submit_id_request,
            padx=30,
            pady=12
        )
        submit_btn.pack(pady=20)
    
    def submit_id_request(self):
        request_id = "ID" + str(random.randint(10000, 99999))
        message = f"✓ ID Card Request Submitted!\n\n"
        message += f"Request ID: {request_id}\n"
        message += f"Service Type: {self.id_service.get()}\n"
        message += f"Status: Processing\n\n"
        message += "Your request has been forwarded to the ID Card Office.\n"
        message += "You can collect your ID card from the Admin Office within 3-5 business days.\n\n"
        message += "Please bring this Request ID and your current student ID for verification."
        
        messagebox.showinfo("Request Confirmation", message)
    
    def open_documents(self):
        self.clear_panel()
        
        title = tk.Label(
            self.right_panel,
            text="📜 Document Collection Services",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        title.pack(pady=20)
        
        # Document Type
        doc_frame = tk.Frame(self.right_panel, bg=self.colors['bg_medium'])
        doc_frame.pack(pady=20, fill='both', expand=True, padx=40)
        
        tk.Label(
            doc_frame,
            text="Select Document Type:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 15))
        
        self.doc_type = tk.StringVar(value="Transcript")
        
        documents = [
            "Transcript",
            "Degree Certificate",
            "Bonafide Certificate",
            "No Objection Certificate (NOC)",
            "Character Certificate",
            "Course Completion Certificate"
        ]
        
        for doc in documents:
            tk.Radiobutton(
                doc_frame,
                text=doc,
                variable=self.doc_type,
                value=doc,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(anchor='w', pady=5)
        
        # Number of Copies
        copies_frame = tk.Frame(doc_frame, bg=self.colors['bg_medium'])
        copies_frame.pack(anchor='w', pady=20)
        
        tk.Label(
            copies_frame,
            text="Number of Copies:",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(side='left', padx=(0, 10))
        
        self.num_copies = tk.Spinbox(
            copies_frame,
            from_=1,
            to=10,
            font=("Helvetica", 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            width=10
        )
        self.num_copies.pack(side='left')
        
        # Purpose
        tk.Label(
            doc_frame,
            text="Purpose of Document:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(20, 10))
        
        self.doc_purpose = scrolledtext.ScrolledText(
            doc_frame,
            height=3,
            width=60,
            font=("Helvetica", 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary']
        )
        self.doc_purpose.pack(anchor='w')
        
        # Submit Button
        submit_btn = tk.Button(
            self.right_panel,
            text="Request Document",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg='white',
            activebackground=self.colors['accent_hover'],
            relief='flat',
            cursor='hand2',
            command=self.submit_doc_request,
            padx=30,
            pady=12
        )
        submit_btn.pack(pady=20)
    
    def submit_doc_request(self):
        request_id = "DOC" + str(random.randint(10000, 99999))
        message = f"✓ Document Request Submitted!\n\n"
        message += f"Request ID: {request_id}\n"
        message += f"Document Type: {self.doc_type.get()}\n"
        message += f"Copies: {self.num_copies.get()}\n"
        message += f"Status: Processing\n\n"
        message += "Your document will be ready for collection within 5-7 business days.\n"
        message += "Collection Location: Registrar's Office, Building A\n"
        message += "Office Hours: Monday-Friday, 9:00 AM - 4:00 PM\n\n"
        message += "Please bring your student ID for verification."
        
        messagebox.showinfo("Request Confirmation", message)
    
    def open_course_registration(self):
        self.clear_panel()
        
        title = tk.Label(
            self.right_panel,
            text="📚 Course Registration",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        title.pack(pady=20)
        
        # Registration Type
        reg_frame = tk.Frame(self.right_panel, bg=self.colors['bg_medium'])
        reg_frame.pack(pady=20, fill='both', expand=True, padx=40)
        
        tk.Label(
            reg_frame,
            text="Registration Type:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 15))
        
        self.reg_type = tk.StringVar(value="Add Course")
        
        for reg_type in ["Add Course", "Drop Course", "Swap Course"]:
            tk.Radiobutton(
                reg_frame,
                text=reg_type,
                variable=self.reg_type,
                value=reg_type,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(anchor='w', pady=5)
        
        # Course Code
        tk.Label(
            reg_frame,
            text="Course Code:",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(20, 5))
        
        self.course_code = tk.Entry(
            reg_frame,
            font=("Helvetica", 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary'],
            width=30
        )
        self.course_code.pack(anchor='w')
        self.course_code.insert(0, "CS401")
        
        # Course Name
        tk.Label(
            reg_frame,
            text="Course Name:",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(15, 5))
        
        self.course_name = tk.Entry(
            reg_frame,
            font=("Helvetica", 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary'],
            width=50
        )
        self.course_name.pack(anchor='w')
        self.course_name.insert(0, "Advanced Database Systems")
        
        # Reason
        tk.Label(
            reg_frame,
            text="Reason for Add/Drop:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(20, 10))
        
        self.course_reason = scrolledtext.ScrolledText(
            reg_frame,
            height=3,
            width=60,
            font=("Helvetica", 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary']
        )
        self.course_reason.pack(anchor='w')
        
        # Submit Button
        submit_btn = tk.Button(
            self.right_panel,
            text="Submit Registration Request",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg='white',
            activebackground=self.colors['accent_hover'],
            relief='flat',
            cursor='hand2',
            command=self.submit_course_request,
            padx=30,
            pady=12
        )
        submit_btn.pack(pady=20)
    
    def submit_course_request(self):
        request_id = "CRS" + str(random.randint(10000, 99999))
        message = f"✓ Course Registration Request Submitted!\n\n"
        message += f"Request ID: {request_id}\n"
        message += f"Type: {self.reg_type.get()}\n"
        message += f"Course: {self.course_code.get()} - {self.course_name.get()}\n"
        message += f"Status: Pending Academic Advisor Approval\n\n"
        message += "You will receive an email notification once your request is processed. Processing typically takes 1-2 business days."
        
        messagebox.showinfo("Request Confirmation", message)
    
    def open_scholarship(self):
        self.clear_panel()
        
        title = tk.Label(
            self.right_panel,
            text="💰 Scholarship & Financial Aid",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        )
        title.pack(pady=20)
        
        # Create a canvas with scrollbar for the form
        canvas = tk.Canvas(self.right_panel, bg=self.colors['bg_medium'], highlightthickness=0)
        scrollbar = tk.Scrollbar(self.right_panel, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_medium'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True, padx=(40, 0))
        scrollbar.pack(side="right", fill="y", padx=(0, 40))
        
        # Scholarship Type - now using scrollable_frame instead of schol_frame
        schol_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_medium'])
        schol_frame.pack(pady=20, fill='both', expand=True, padx=20)
        
        tk.Label(
            schol_frame,
            text="Select Financial Aid Type:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(0, 15))
        
        self.aid_type = tk.StringVar(value="Merit-Based Scholarship")
        
        aid_types = [
            "Merit-Based Scholarship",
            "Need-Based Financial Aid",
            "Sports Scholarship",
            "Research Grant",
            "Emergency Financial Assistance",
            "Tuition Waiver Application"
        ]
        
        for aid in aid_types:
            tk.Radiobutton(
                schol_frame,
                text=aid,
                variable=self.aid_type,
                value=aid,
                font=("Helvetica", 11),
                bg=self.colors['bg_medium'],
                fg=self.colors['text_primary'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_medium']
            ).pack(anchor='w', pady=5)
        
        # GPA
        gpa_frame = tk.Frame(schol_frame, bg=self.colors['bg_medium'])
        gpa_frame.pack(anchor='w', pady=20)
        
        tk.Label(
            gpa_frame,
            text="Current GPA:",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(side='left', padx=(0, 10))
        
        self.gpa = tk.Entry(
            gpa_frame,
            font=("Helvetica", 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary'],
            width=10
        )
        self.gpa.pack(side='left')
        self.gpa.insert(0, "3.85")
        
        # Family Income
        income_frame = tk.Frame(schol_frame, bg=self.colors['bg_medium'])
        income_frame.pack(anchor='w', pady=10)
        
        tk.Label(
            income_frame,
            text="Annual Family Income ($):",
            font=("Helvetica", 11),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(side='left', padx=(0, 10))
        
        self.income = tk.Entry(
            income_frame,
            font=("Helvetica", 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary'],
            width=15
        )
        self.income.pack(side='left')
        self.income.insert(0, "45000")
        
        # Statement
        tk.Label(
            schol_frame,
            text="Personal Statement / Need Justification:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['bg_medium'],
            fg=self.colors['text_primary']
        ).pack(anchor='w', pady=(20, 10))
        
        self.statement = scrolledtext.ScrolledText(
            schol_frame,
            height=5,
            width=60,
            font=("Helvetica", 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary']
        )
        self.statement.pack(anchor='w')
        
        # Submit Button - now inside scrollable_frame
        submit_btn = tk.Button(
            schol_frame,
            text="Submit Application",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg='white',
            activebackground=self.colors['accent_hover'],
            relief='flat',
            cursor='hand2',
            command=self.submit_scholarship_application,
            padx=30,
            pady=12
        )
        submit_btn.pack(pady=30)
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def submit_scholarship_application(self):
        # Validate input
        if not self.gpa.get().strip():
            messagebox.showerror("Validation Error", "Please enter your GPA.")
            return
        
        if not self.income.get().strip():
            messagebox.showerror("Validation Error", "Please enter your family income.")
            return
        
        if not self.statement.get("1.0", "end-1c").strip():
            messagebox.showerror("Validation Error", "Please provide a personal statement.")
            return
        
        # Generate application details
        app_id = "SCH" + str(random.randint(10000, 99999))
        
        # Determine eligibility message based on GPA
        try:
            gpa_value = float(self.gpa.get())
            if gpa_value >= 3.5:
                eligibility_note = "Your excellent academic record strengthens your application."
            elif gpa_value >= 3.0:
                eligibility_note = "Your academic standing meets the minimum requirements."
            else:
                eligibility_note = "Note: Some scholarships require a minimum GPA of 3.0."
        except ValueError:
            eligibility_note = "Please ensure GPA is entered correctly."
        
        message = f"✓ Scholarship Application Submitted Successfully!\n\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"Application ID: {app_id}\n"
        message += f"Applicant: {self.student_name}\n"
        message += f"Student ID: {self.student_id}\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        message += f"Application Type: {self.aid_type.get()}\n"
        message += f"GPA: {self.gpa.get()}\n"
        message += f"Annual Family Income: ${self.income.get()}\n\n"
        message += f"{eligibility_note}\n\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"NEXT STEPS:\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        message += f"1. Your application has been forwarded to the Financial Aid Committee\n"
        message += f"2. Review process: 2-3 weeks\n"
        message += f"3. You may be contacted for additional documentation\n"
        message += f"4. Interview (if shortlisted): Week of {datetime.now().strftime('%B %d, %Y')}\n\n"
        message += f"You will receive email updates at your registered university email address.\n\n"
        message += f"For inquiries, contact: financialaid@university.edu\n"
        message += f"Reference your Application ID: {app_id}"
        
        messagebox.showinfo("Application Confirmation", message)

def main():
    root = tk.Tk()
    app = CollegeUtilityHub(root)
    root.mainloop()

if __name__ == "__main__":
    main()
