public class Journal
{
    public string _name;
    public List<Entry> _entry = new List<Entry>();

    public List<ImportantDate> _importantDate = new List<ImportantDate>();

    public void Display()
    {
        foreach (Entry entry in _entry)
        {
            entry.Display();
        }
    }

        public void DisplayImportantDate()
    {
        foreach (ImportantDate importantDate in _importantDate)
        {
            importantDate.Display();
        }
    }

        public void Save(Entry entry)
    {
            _entry.Add(entry);
    }

        public void SaveImportantDate(ImportantDate importantDate)
    {
            _importantDate.Add(importantDate);
    }
        public void SaveFile()
    { 
        Console.WriteLine("");
        Console.Write("What is the file you would like to save? Include the extension example file.txt?\n");
        string filename = Console.ReadLine();
        using (StreamWriter outputFile = new StreamWriter(filename))
        foreach (Entry entry in _entry)
        {
            outputFile.WriteLine($"Date: {entry._date} - Prompt: {entry._prompt}");
            outputFile.WriteLine($"{entry._entry}");
        }
    }

        public void SaveImportantEventFile()
    { 
        Console.WriteLine("");
        Console.Write("What is the file you would like to import? Include the extension example file.txt?\n");
        string filename = Console.ReadLine();
        using (StreamWriter outputFile = new StreamWriter(filename))
        foreach (ImportantDate importantDate in _importantDate)
        {
            outputFile.WriteLine($"Date: {importantDate._date}");
            outputFile.WriteLine($"{importantDate._importantDate}");
        }
    }

        public void LoadFile()
    { 
        Console.WriteLine("");
        Console.Write("What is the file you would like to load? Include the extension example file.txt\n");
        string filename = Console.ReadLine();

        string[] lines = System.IO.File.ReadAllLines(filename);
        Console.WriteLine("");
        foreach (string line in lines)
        {
            Console.WriteLine(line);
        }
    }
}