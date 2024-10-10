# Vaktija to iCalendar Converter

This script converts prayer times from the Vaktija API to an iCalendar (.ics) file, which can be imported into your desired calendar application (Microsoft Outlook, Google Calendar, Apple Calendar, etc.).

## Steps to Use

1. **Find Your Location ID**

   - Go to Vaktija API Locations.
   - Find the location ID for your town. For example, the ID for Sarajevo is `77`.

2. **Get the JSON Data**

   - Choose the year you need to convert.
   - Go to `https://api.vaktija.ba/vaktija/v1/town_id/year`. For example, for Sarajevo in 2024, the URL would be `https://api.vaktija.ba/vaktija/v1/77/2024`.
   - Copy the JSON data from the API response.

3. **Create the JSON File**

   - In the root folder of this repository, create a file named `year.json`.
   - Paste the copied JSON data into `year.json`.

4. **Run the Script**

   - Make sure you have Python installed on your system.
   - Run the script using the command:
     ```sh
     python vaktija.py
     ```

5. **Import the .ics File**
   - The script will generate a file named `prayer_times.ics`.
   - Import this file into your desired calendar application.

## Example

For Sarajevo in 2024:

1. Go to `https://api.vaktija.ba/vaktija/v1/77/2024`.
2. Copy the JSON data.
3. Create `year.json` in the root folder and paste the data.
4. Run the script:
   ```sh
   python vaktija.py
   ```
