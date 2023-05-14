using System;
using System.IO; 

class Program
{
    static void Main(string[] args)
    {
        int inputNumber;
        string entry;
        string dateText;
        string prompt;
        List<Entry> _entryList = new List<Entry>();
        Journal myJournal = new Journal();
        RandomPrompt random =  new RandomPrompt();
        
            do
            {
                Console.WriteLine("");
                Console.Write("Welcome to the Journal Program What would you like to do? Enter the number corisponding to the action you would like to do.\n");
                Console.WriteLine("");
                Console.Write("1. Write\n");
                Console.Write("2. Display\n");
                Console.Write("3. Load\n");
                Console.Write("4. Save\n");
                Console.Write("5. Record Important event/entry\n");
                Console.Write("6. Display Important entries/events\n");
                Console.Write("7. Load Important entries/events\n");
                Console.Write("8. Save Important entires/events\n");
                Console.Write("9. Quit\n");
                Console.WriteLine("");
                string userInput = Console.ReadLine();
                inputNumber = int.Parse(userInput);

                if (inputNumber == 1)
                {
                    prompt = random.Display();
                    Console.WriteLine("");
                    Console.Write($"{prompt}\n");
                    entry = Console.ReadLine();
                    DateTime theCurrentTime = DateTime.Now;
                    dateText = theCurrentTime.ToShortDateString();
                    Entry myEntry = new Entry();
                    myEntry._date = dateText;
                    myEntry._entry = entry;
                    myEntry._prompt = prompt;
                    myJournal.Save(myEntry);
                }
                else if (inputNumber == 2)
                {
                    myJournal.Display();
                }
                else if (inputNumber == 3)
                {
                    myJournal.LoadFile();
                } 
                else if (inputNumber == 4)
                {
                    myJournal.SaveFile();
                }
                else if (inputNumber == 5)
                {
                    Console.WriteLine("");
                    Console.Write("Enter The date in the following format: MM/DD/YYYY example: 02/20/2023\n");
                    string date = Console.ReadLine();
                    Console.WriteLine("");
                    Console.Write("Why is this day important? \n");
                    string importantDate = Console.ReadLine();
                    ImportantDate myImportantDate = new ImportantDate();
                    myImportantDate._date = date;
                    myImportantDate._importantDate = importantDate;
                    myJournal.SaveImportantDate(myImportantDate);
                }
                else if (inputNumber == 6)
                {
                    myJournal.DisplayImportantDate();
                }
                else if (inputNumber == 7)
                {
                    myJournal.LoadFile();
                } 
                else if (inputNumber == 8)
                {
                    myJournal.SaveImportantEventFile();
                }
 
            } while (inputNumber != 9);
            Console.Write("Farewell travler.\n");
    }
}