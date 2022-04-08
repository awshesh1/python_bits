{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "40f25083",
   "metadata": {},
   "source": [
    "## This is an attempt to code the caesar cipher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2519f64c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ceaser_cipher(word,move):\n",
    "    string= word\n",
    "    caeser_word = str()\n",
    "    word_basket = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',\n",
    "                7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',\n",
    "              13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',\n",
    "              19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',\n",
    "              25:'Y',26:'Z'}\n",
    "    key_list = list(word_basket.keys())\n",
    "    value_list = list(word_basket.values())\n",
    "    for letter in string:\n",
    "        if letter == ' ':\n",
    "            caeser_word = caeser_word + ' '\n",
    "        else:\n",
    "            letter = letter.upper()\n",
    "            position = value_list.index(letter)\n",
    "            old_key = key_list[position]\n",
    "            new_key = old_key+move\n",
    "            if new_key > 26:\n",
    "                new_key = new_key%26\n",
    "            elif new_key < 1:\n",
    "                new_key = 26-new_key%26\n",
    "            else:\n",
    "                new_key=new_key\n",
    "            new_letter = word_basket[new_key]\n",
    "            caeser_word = caeser_word+new_letter\n",
    "    print(caeser_word)\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "083c5024",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please provide input caesar>>>--James bond is hocus pocus\n"
     ]
    }
   ],
   "source": [
    "word = input(\"Please provide input caesar>>>--\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b11e8f85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NWKSE VIJT OE PIUCE HIUCE\n"
     ]
    }
   ],
   "source": [
    "ceaser_cipher(word,-50)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
