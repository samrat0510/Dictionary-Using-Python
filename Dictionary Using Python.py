{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "055d5e62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the word you want the meaning of:paper\n",
      "Felted or matted sheets of cellulose fibers, formed on a fine-wire screen from a dilute water suspension, and bonded together as the water is removed and the sheet is dried.\n",
      "Made of paper.\n",
      "A scholarly written work describing the results of observations or stating hypotheses.\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "from difflib import get_close_matches\n",
    "data= json.load(open(\"data.json\"))\n",
    "\n",
    "def translate(word):\n",
    "    if word in data:\n",
    "        return data[word]\n",
    "    elif word.title() in data:\n",
    "        return data[word.title()]\n",
    "    elif word.upper() in data:\n",
    "        return data[word.upper()]\n",
    "    elif len(get_close_matches(word, data.keys()))>0:\n",
    "        print(\"Did you mean %s instead\" %get_close_matches(word, data.keys())[0])\n",
    "        decide=input(\"Press Y for yes and N for no.\")\n",
    "        if decide==\"y\":\n",
    "            return data[get_close_matches(word, data.keys())[0]]\n",
    "        elif decide==\"n\":\n",
    "            return(\"Wrong word. Please try again.\")\n",
    "    else:\n",
    "        print(\"Word doesn't exist in the data.\")\n",
    "        \n",
    "word=input(\"Enter the word you want the meaning of:\")\n",
    "output=translate(word)\n",
    "if type(output)==list:\n",
    "    for i in output:\n",
    "        print(i)\n",
    "else:\n",
    "    print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70807f3f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b01f766",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
