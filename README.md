# **AquaLink: Enhancing Urban Water Delivery Through Smart Logistics**

AquaLink is an innovative platform designed to address urban water delivery challenges. It streamlines the process of ordering, tracking, and delivering water cans, ensuring reliable and efficient service for households, offices, and events.

---

## **Introduction**
With the increasing demand for clean water in urban areas, AquaLink aims to bridge the gap between suppliers and consumers through a user-friendly web application. The platform offers real-time tracking, secure payment options, and certified suppliers to guarantee water quality and timely delivery.

---

## **How the Website Works**

1. **User Registration and Login**
   - New users can register by providing their details (name, phone number, email, and password).
   - Existing users can log in with their phone number and password.

2. **Place an Order**
   - Users can select the desired quantity of water cans and schedule delivery.

3. **Real-Time Tracking**
   - Once an order is placed, users can track the delivery status in real time.

4. **Backend Integration**
   - The platform is powered by a Flask backend with MongoDB for database management.

5. **Secure and Efficient**
   - Passwords are hashed for security, and all interactions are managed via RESTful APIs.

---

## **Features**
- User-friendly interface for ordering water cans.
- Real-time order tracking and status updates.
- Secure user authentication with hashed passwords.
- Reliable database management using MongoDB.

---

## **Technologies Used**
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **APIs**: RESTful APIs for seamless communication

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.8+
- MongoDB (Installed and Running)

### **2. Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/AquaLink.git
   cd AquaLink

### **3. Installation Steps**

1. Install Dependencies:
Run the following command to install the required dependencies:
  ```bash
  pip install flask pymongo werkzeug
```
2. Start MongoDB:
Ensure MongoDB is running on the default port 27017.

Run the application:

  ```bash
  python app.py
  Open the website in your browser:
  Visit http://127.0.0.1:5000
  ```

## **Future Scope**
- Expand to mobile platforms with React Native.
- Integrate advanced analytics for order predictions.
- Scale the platform to support multiple cities.
- Contributing
- We welcome contributions to improve AquaLink!
- Please submit a pull request or open an issue for suggestions.

## **License**
- This project is licensed under the MIT License.
