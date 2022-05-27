exports.isCharacterMatch = function(string1, string2) {

    string1 = string1.toLowerCase().replace(/ /g, "")
    string2 = string2.toLowerCase().replace(/ /g, "")

    string1 = string1.split("")
    string2 = string2.split("")

    string1 = string1.sort()
    string2 = string2.sort()

    string1 = string1.join("")
    string2 = string2.join("")

    return string1 === string2
};


