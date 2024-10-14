# Digital Clock

This application implements a modern digital clock using the Tkinter library in Python, providing a visually appealing and functional interface that continuously updates to display the current time and date.

## Overview

The digital clock application serves as a real-time representation of the current time, complete with the day of the week and the date. Built using Tkinter, it features a sleek black background and vibrant green text, optimizing readability. The clock leverages the `datetime` module to fetch and format the current time and updates its display every second, ensuring users have access to accurate time information at all times.

## Features

- **User-Friendly GUI**: The application utilizes Tkinter to create an intuitive and visually engaging graphical user interface (GUI) that enhances the user experience with minimal cognitive load.
- **Real-Time Updates**: The clock employs a periodic refresh mechanism to update its display every second, providing a precise and accurate time representation.
- **Precise Time Formatting**: The application formats the time in a 12-hour format (with AM/PM) alongside the current day of the week and date, utilizing `strftime` for flexible string formatting.
- **Dynamic Interaction**: The text color is configured to change upon mouse hover events, enhancing interactivity and providing visual feedback to the user.

## Screenshots

The application features a real-time digital clock displayed within a Tkinter window. Below are examples of the clock in action:

- **Default View**: Displays the current time, day, and date in a prominent format.
- **Hover Effect**: Illustrates the dynamic text color change in response to mouse enter and leave events.
  
![Screenshot 2024-10-14 183805 (1)](https://github.com/user-attachments/assets/a66a02ae-7a04-45fc-8854-0e92d23c326d)


## Getting Started

To run the application, ensure you have Python (version 3.x recommended) installed along with the Tkinter library, which is typically included with standard Python installations. Clone this repository using the following command:

```bash
git clone https://github.com/yourusername/digital-clock.git
