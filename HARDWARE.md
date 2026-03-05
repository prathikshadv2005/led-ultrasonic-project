# 🔌 Circuit Wiring

## 📍 Connections

### Ultrasonic Sensor

| HC-SR04 Pin | Raspberry Pi 4 Pin | GPIO                         |
| ----------- | ------------------ | ---------------------------- |
| VCC         | Pin 2              | 5V                           |
| GND         | Pin 6              | GND                          |
| TRIG        | Pin 16             | GPIO23                       |
| ECHO        | Pin 18             | GPIO24 (via voltage divider) |

### LED

| LED Pin     | Raspberry Pi 4 Pin    | GPIO   |
| ----------- | --------------------- | ------ |
| Anode (+)   | Pin 11                | GPIO17 |
| Cathode (-) | GND via 220Ω resistor | GND    |

---

## ⚠️ Voltage Divider for ECHO

The ECHO pin outputs **5V**, but Raspberry Pi GPIO works at **3.3V**.

Use:

* **1kΩ resistor** between ECHO and GPIO24
* **2kΩ resistor** between GPIO24 and GND

This reduces **5V to ~3.3V** and protects the Raspberry Pi.

---

## 💡 LED Operation

* When the **distance is less than 5 cm → LED turns ON**
* When the **distance is greater than 5 cm → LED turns OFF**

---

## 📷 Circuit Diagram

<img width="1536" height="803" alt="image" src="PASTE_YOUR_LED_ULTRASONIC_CIRCUIT_IMAGE_LINK_HERE" />
