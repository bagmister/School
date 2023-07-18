using System;


namespace Mindfullness
{
    class Program
    {
        public static void Main(string[] args)
        {
            var UserChoice = 0;
            var EndingMessage = "";
            var ApplicationName = "";
             while (UserChoice != 4)
            {
                    Console.Write("Welcom to the wellness program? Enter 1 for breathing. Enter 2 for Meditation. Enter 3 for listening. Enter 4 to exit.");
                    UserChoice = int.Parse(Console.ReadLine());
                    if (UserChoice == 1)
                    {
                        ApplicationName = "Breathing";
                        Console.WriteLine($"We will be starting the {ApplicationName} activity");
                    }
                    else if (UserChoice == 2)
                    {
                        ApplicationName = "Meditation";
                        Console.WriteLine($"{ApplicationName} activity");
                    }
                    else if (UserChoice == 3)
                    {
                        ApplicationName = "Listening";
                        Console.WriteLine($"{ApplicationName} activity");
                    }
                    else
                    {
                        Console.WriteLine("Exiting Program. I bid you farewell!");
                    }
            }
            Console.WriteLine($"{EndingMessage}");
        }
    }
}