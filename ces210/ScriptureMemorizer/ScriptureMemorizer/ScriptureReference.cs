using System;
namespace ScirptureMemeorizer;
public class ScriptureReference
{
    private string _reference = "Isaiah 41:10-13";
    private int _verse1 = 10;
    private int _verse2 = 11;
    private int _verse3 = 12;
    private int _verse4 = 13;
    private string _verse1Text = "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.";
    private string _verse2Text = "Behold, all they that were incensed against thee shall be ashamed and confounded: they shall be as nothing; and they that strive with thee shall aperish.";
    private string _verse3Text = "Thou shalt seek them, and shalt not find them, even them that contended with thee: they that war against thee shall be as nothing, and as a thing of nought.";
    private string _verse4Text = "For I the Lord thy God will hold thy right hand, saying unto thee, Fear not; I will help thee.";


    public string GetReference()
    { 
        return _reference;
    }

    public int Getverse1()
    {
        return _verse1;
    }
    public int Getverse2()
    {
        return _verse2;
    }
    public int Getverse3()
    {
        return _verse3;
    }
    public int GetVerse4()
    {
        return _verse4;
    }
    public string GetVerse1Text()
    {
        return _verse1Text;
    }
    public string GetVerse2Text()
    {
        return _verse2Text;
    }
    public string GetVerse3Text()
    {
        return _verse3Text;
    }
    public string GetVerse4Text()
    {
        return _verse4Text;
    }
}
