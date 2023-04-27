using System;


class MagicNumber
{
    static void Main(string[] args)
    {
        var magicRandmom = new Random();
        var Magicnumber = magicRandmom.Next(1,101);
        var UserGuess = -1;
        while (UserGuess != Magicnumber)
        {
            Console.Write("What is your guess?");
            UserGuess = int.Parse(Console.ReadLine());
            if (UserGuess > Magicnumber)
            {
                Console.WriteLine("Higher");
            }
            else if (UserGuess < Magicnumber)
            {
                Console.WriteLine("Lower");
            }
            else
            {
                Console.WriteLine("You Guessed it!");
            }

        }
    }
}
