# Rural School Attendance System

A simple, offline-capable web application for managing student attendance in rural schools.

## Features

- Add and manage students
- Mark daily attendance
- View attendance records
- Works completely offline
- Responsive design for all devices

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/attendance-system.git
   cd attendance-system
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to: `http://127.0.0.1:5000/`

3. Start by adding students, then mark their attendance.

## Deployment

### Option 1: Local Network Access

To make the app accessible on your local network, modify the last line in `app.py` to:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Then other devices on the same network can access it using your computer's local IP address.

### Option 2: Deploy to a VPS

For wider access, you can deploy to a VPS like DigitalOcean, Linode, or AWS EC2.

## License

MIT
