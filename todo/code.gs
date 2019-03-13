#google spreadsheet file to be embeded in the script part to make the sheets running all
#time and adding events to your calender so that you cna get all events reminders mails etc.




function myFunction() {
  var Spreadsheet = SpreadsheetApp.getActiveSheet();
  var calenderId = spreadsheet.getRange("C4").getValue();
  var event = CalenderApp.getCalenderById("calenderId");
  var signup = spreadsheet.getRange("A8","C12");
  for (x = 0; x<signups.lenght; x++)
  {
    var shifts = signups[x];
    var starttime = shoft[0];
    var volunteers = shift[2];
    
    eventCal.createEvnt(task,StartTime);
  }
  
}