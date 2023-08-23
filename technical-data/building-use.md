# Building Use Diary

You need to understand when users are in your building and what your occupancy rate is like for four reasons:  

- to inform whether it's worth making changes to make your building more attractive to local groups that need space, so you can get more income.
- to give a sense of how much waste is involved in heating suites of rooms together and whether it might be worth heating some independently.  
- to help you understand which of the heating energy efficiency controls are the right ones to use in your circumstances.  
- when used with temperature data, to help you think about whether users are comfortable and what they might be doing if they are not.

Whoever takes care of bookings should have this information.  

One way to capture it is by taking screenshots of the calendaring system over some typical periods.  If you do this, be mindful of personal and sensitive details.  Addiction and domestic violence support groups often do not want their meeting location widely known, and data protection regulations require you to be careful with personal details like phone numbers.   You could use Microsoft Paint to blank out any of your users' personal or sensitive details before passing them to others.  It is useful if it's possible to tell something about what sort of group it is - children running around versus older adults sitting still, for instance.

Many calendaring systems will allow you to export the entries between two dates in a standard format, an ".ics" file.  More tech-savvy professionals will know how to view this file in their own calendaring system.  Google Calendar and some other systems have the option to share or export a completely anonymised "Busy/Free" version that only shows whether there is something in the calendar or not.  This can be a useful feature.  Web-based booking systems also usually show an anonymised calendar to people who might want to hire a room.

```{admonition}  Better than nothing

Even just knowing which mornings, afternoons, and evenings a week the building is usually occupied is helpful, for instance, in a table like this:

|       |   Mon   | Tues  | Wed   | Thu   | Fri   | Sat   | Sun   |
| :---  | ---     | ---   | ---   | ---   | ---   | ---   | ---:  |
| hall  |A        | P     |  E    |       | APE   |       |       |
| office|A        |A      |A      |A      |A      |       |       |

This building's hall usually has at least some use on Monday mornings, Tuesday afternoons, Wednesday evenings, and all three on Fridays, and usually empty otherwise.   The office is occupied on weekday mornings.
```




```{admonition} A problem we're trying to solve

In session 3, the engineer has to think quickly to match up the temperature data with the building use diary in their heads. We know how to create plots on our website that make this very easy, but it's hard to know how groups should record their diaries because they find different formats convenient.  For venues with very regular schedules, we recommend a spreadsheet like this:  


|Day of week |	Start time|	End time|	Location|	Notes (optional)|
| :---  | ---     | ---   | ---   | ---:  |
|Monday|	9:00	|10:00|	main_hall|	 big active adult group|
|Friday	|10:00|	12:30|	little_hall|	sedentary older adults|

We have a template available for this approach:

- [HeatHack Building Use Diary Template](https://docs.google.com/spreadsheets/d/1_3UwlKGqtnaVQqrsQDyNMr6MdldH_sSLpiHTBwC7AbQ/)

We already know how to show this against the temperature data on-line, but haven't made that public because groups haven't chosen to give us diaries this way.

For venues with variable schedules using a hall management system or calendar service to manage room bookings, there is a better option: exporting your venue diary (or individual room diaries) as ".ics" files from your calendaring system.  Some systems allow "busy/free" views to be exported that remove all personal details.  This could be very useful for data protection, but isn't universal.  We don't have the computer programming in place to use these, but it is easy to do.

Some engineers choose to make their own solution in a spreadsheet.  We have templates for this in Google Sheets and Excel.  Google Sheets will work for everyone but the Excel template requires a very modern version of Excel.

- [Google Sheets example](https://docs.google.com/spreadsheets/d/1GdxF74vFXmlne7ofVjHb_SX-jD8ghrtRD2SeYu5aoTE/)
- [Excel example (Excel for Microsoft 365 and Excel for the web only)](https://docs.google.com/spreadsheets/d/10da4Te3d8atx4GISDbH4W2AW8uisLF4S/)



``````
