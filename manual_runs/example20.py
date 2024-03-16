def remove_that(phrase):
    if "that" in phrase:
        updated_phrase = phrase.replace("that", "")
        return updated_phrase
    else:
        return phrase