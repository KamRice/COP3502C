from cow import Cow


def get_cows():
    cow_names = ["heifer", "kitteh"]

    quote_lines = "    \\\n"
    quote_lines += "     \\\n"
    quote_lines += "      \\\n"

    cow_images = [
        "        ^__^\n"
        + "        (oo)\\_______\n"
        + "        (__)\\       )\\/\\\n"
        + "            ||----w |\n"
        + "            ||     ||\n",
        "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
        + "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
        + "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
        + "      _.. `--'_..-_/   /--' _ .' ,4\n"
        + "   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
    ]
    cows = [None] * len(cow_images)
    for index in range(len(cows)):
        cows[index] = Cow(cow_names[index])
        cows[index].set_image(quote_lines + cow_images[index])
    return cows
