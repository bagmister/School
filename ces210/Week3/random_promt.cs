public class RandomPrompt
{
    IDictionary<int, string> _prompts = new Dictionary<int, string>() {
	{0, "What did you do at 3 pm today?"},
	{1, "What adventure did you embark on today?"},
	{2, "When did you help someone today?"},
    {3, "What went well today?"},
	{4, "What happened to your oldest child today if you have a child? If you don't have a child what about a friend?"},
    {5, "What where some positive things that happened today?"},
    {6, "How have you see nthe Lord bless you as you have served in your calling(s)?"},
    {7, "In what way did you feel the sprit today?"},
    {8, "How did you show your spouse today that you love them? How did you server them today?"}
};

    public string Display()
    {
        Random randomGenerator = new Random();

        int number = randomGenerator.Next(0, 9);

        string prompt =  _prompts[number];
        return prompt;
    }
}