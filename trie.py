# FIT2004 ASSIGNMENT 3
# PRASHANT MURALI - 29625564

import sys

# TASK 1
class TrieNode():
    """
    This TrieNode class is essentially an implementation for the node.
    """
    def __init__(self):
        """
        Initializer for the class.
        Time complexity: Best: O(1)
                         Worst: O(1)
        Space complexity: Best: O(1)
                          Worst: nk (num of records that match id_prefix) or nl (num of records
                          that match last_name_prefix).
        Error handle: None
        Return: None
        Parameter: None
        Precondition: None
        """
        # Initialize the lists where the numbers and alphabets will be placed.
        # 62 spaces because 10 numbers + 26 lowercase letters + 26 uppercase letters.
        self.children = [None]*62
        # This list would hold the index of which that character from the record was placed.
        self.index_list=[]
        self.match=False
        self.character=None
        self.checked=False

def splitSpace(file_list):
    """
    This function splits whitespace between characters and puts them into a list.
    Time complexity:  Best: O(NM)
                      Worst: O(NM)
    Space complexity:  Best: O(NM)
                       Worst: O(NM)
    Error handle: None
    Return: A list with lists of the items in the row from data in the database.
    Parameter: file_list, which is a list that contains the data that has already
                been split by newlines.
    Precondition: Parameter must be a file of rows divided by newlines.
    """
    word=""
    list1=[]
    list2=[]
    for index in range(len(file_list)):
        for item in range(len(file_list[index])):
            # If the character is not a whitespace, it is added to the list.
            if file_list[index][item] != ' ':
                word += file_list[index][item]
                if item == (len(file_list[index]) - 1):
                     list1.append(word)
                     word=""
            else:
                list1.append(word)
                word = ""
        # The list is then added to the final list which is list2.
        list2.append(list1)
        list1=[]
    return list2

def splitNewLine(file):
    """
    This function splits the rows in the database file (between newlines).
    Time complexity:  Best: O(NM)
                      Worst: O(NM)
    Space complexity:  Best: O(NM)
                       Worst: O(NM)
    Error handle: None
    Return: A list with each row in the database file.
    Parameter: file, which is the data from the database file.
    Precondition: The parameter must be a list with each row as an item in it.
    """
    word=""
    input_file=[]
    for index in range(len(file)):
        # If the current character is not a newline, it is added to the list.
        if file[index] != '\n':
            word += file[index]

            if index == (len(file) - 1):
                input_file.append(word)
        else:
            # Basically gets split when there is a newline.
            input_file.append(word)
            word = ""
    return input_file

def getIndex(char):
    """
    This function gets the index of the character that is passed into the function.
    Time complexity:  Best: O(1)
                      Worst: O(1)
    Space complexity:  Best: O(1)
                       Worst: O(1)
    Error handle: None
    Return: The index value for that character.
    Parameter: char, which is the character that needs to get its index found.
    Precondition: parameter character must be lowercase/uppercase letters and integers only.
    """
    # If the ord value of the char is less than 57, it is taken as a digit (0,1...9),
    # and its appropriate index is returned.
    if ord(char)<=57:
        index=ord(char)-48
    # If the ord value of the char is less than 90, it is taken as an uppercase char (A,B...Z),
    # and its appropriate index is returned.
    elif ord(char)<=90:
        index=ord(char)-55
    # If the ord value of the char is less than 122, it is taken as a lowercase char (a,b...z),
    # and its appropriate index is returned.
    elif ord(char)<=122:
        index=ord(char)-61

    # index is returned.
    return index

def addData(root,row):
    """
    This function adds the characters into the Trie.
    Time complexity:  Best: O(T)
                      Worst: O(T)
    Space complexity:  Best: O(T)
                       Worst: O(T)
    Error handle: None
    Return: None, as any changes are simply done in the nodes.
    Parameter: root, which is the initialization of the TrieNode class, and row, which
     is the row of which the id and lastname columns will be added to the Trie.
    Precondition: root must be a reference to the TrieNode class, and row should have all items in it.
    """
    # This would be the last name.
    last_name=row[3]

    # This would be the id.
    id=row[1]

    # This would be the index for the row from which the last names and id are in.
    ind=row[0]

    # Adding the last names into the Trie.
    # Set the node to the root, (the start basically).
    node=root

    for char in last_name:
        # Get the index of the character.
        index=getIndex(char)
        # If the character doesn't exist, create a new Trie at that index.
        if node.children[index]==None:
            node.children[index]=TrieNode()
        # Append that rows index into this positions index_list.
        if node.index_list==[]:
            node.index_list.append(ind)
        elif node.index_list[-1]!=ind:
            node.index_list.append(ind)
        # Set the node to its child now.
        node=node.children[index]

    # Now add the id's into the Trie.
    # Set the node to the root, (back to the start again).
    node=root

    for char in id:
        # Get the index of the character.
        index=getIndex(char)
        # If the character doesn't exist, create a new Trie at that index.
        if node.children[index]==None:
            node.children[index]=TrieNode()
        # Append that rows index into this positions index_list.
        if node.index_list == []:
            node.index_list.append(ind)
        elif node.index_list[-1] != ind:
            node.index_list.append(ind)
        # Set the node to its child now.
        node=node.children[index]

def query(filename, id_prefix, last_name_prefix):
    """
    This function, given a file of records and two parameters, id_prefix and last_name_prefix, finds
    the indices of all records which have an identification number (id) whose prefix is id_prefix and
    last name whose prefix is last_name_prefix.
    Time complexity:  Best: O(k + l + nk + nl) - for the queries only.
                      Worst: O(k + l + nk + nl) - for the queries only.
    Space complexity:  Best: O(T + NM)
                       Worst: O(T + NM)
    Error handle: Upon opening the file, if the file is empty, the function is exited.
    Return: A list of indices.
    Parameter: filename, which is the name of the database, id_prefix, which
     is the prefix of the id that is used to find the id's, and last_name_prefix which
     is the prefix used to find the last names.
    Precondition: filename must exist, id_prefix must be integers, last_name_prefix must be upper/lower
                   case letters.
    """
    # Initialize the TrieNode.
    root=TrieNode()

    # Open the file. Note that errors in the FILENAME has already been checked in the
    # main block, so its no longer checked here.
    # The file however is later checked to see if its empty or not.
    file=open(filename,"r")

    # Read the file.
    file=file.read()

    # If the file is empty, the function is exited.
    if file == "":
        sys.exit()

    # Split the data in the file between newlines. Essentially putting every
    # row as an item into the list.
    file=splitNewLine(file)

    # Now, the items in that list is split for its whitespace.
    list_file=splitSpace(file)

    # Add the items into the Trie. Note that the row is sent in to the add function here.
    # The add function would get the columns for the id and last name in its function.
    for row in (list_file):
        addData(root,row)

    # Now that the data has been added into the Trie, we can query it using the prefix
    # given.

    # Point the node to the root, which is the start of the Trie.
    node = root
    for char in (last_name_prefix):
        index = getIndex(char)
        # If the character in the prefix is not found in the Trie, then an
        # an empty list is returned because it simply means no items had match.
        if node.children[index]==None:
            return []
        # Set the node to its child.
        node = node.children[index]
    # Set the id_index_list to the row indexes found up to this point.
    last_name_index_list=(node.index_list)

    # Now search for the prefix of the last name.

    # Set the node back to the root, (basically going back to the start).
    node = root
    for char in id_prefix:
        index = getIndex(char)
        # If the character in the prefix is not found in the Trie, then an
        # an empty list is returned because it simply means no items had match.
        if node.children[index]==None:
            return []
        # Set the node to its child.
        node = node.children[index]
    # Set the last_name_index_list to the row indexes found up to this point.
    id_index_list=(node.index_list)

    # The list below would hold the final indexes that match in both the id_index_list
    # and last_name_index_list.
    final_index_list=[]

    # Now that we have two lists that contain the matched indexes for the prefix id's and
    # last names, we can find the indexes when both id prefix and last name prefix match are present
    # in the Trie. To do this, when both lists have the same index, it would be taken and placed
    # into the final list, and an efficient method to do this is done below. Note the method done
    # below is applicable only if the two list of indexes are sorted, which in this case they are.

    # Find the smaller list and bigger list correspondingly.
    if len(id_index_list)<len(last_name_index_list):
        smallerlist=id_index_list
        biggerlist=last_name_index_list
    else:
        smallerlist=last_name_index_list
        biggerlist=id_index_list

    i=0
    j=0

    # Loops through the smaller list, so i times as most.
    while i<len(smallerlist):
        # If the indexes match, put them into the final list.
        if int(smallerlist[i])==int(biggerlist[j]):
            final_index_list.append(int(smallerlist[(i)]))
            i+=1
            j+=1
        elif int(smallerlist[i])>int(biggerlist[j]):
            j+=1
        else:
            i+=1

    # The final list is returned.
    return final_index_list


# TASK 2

def reverseSubstrings(filename):
    """
    This function finds all substrings of length > 1 whose reverse also exists in the text.
    Time complexity:  Best: O((K^2 + P)
                      Worst: O((K^2 + P)
    Space complexity:  Best: O(K^2 + P)
                       Worst: O(K^2 + P)
    Error handle: Upon opening the file, if the file is empty, the function is exited.
    Return: A list of lists, where each inner list will contain two values.
    Parameter: filename, which is the file that has the string which will be used.
    Precondition: filename must exist, and characters in lowercase.
    """

    file = open(filename, "r")

    # Read the file.
    file = file.read()

    # If the file is empty, the function is exited.
    if file == "":
        sys.exit()

    # print(file)

    # One variable to hold the original string, and another to hold the reverse of it.
    ori_str=file
    rev_str=file[::-1]

    # Generate all suffixes of the original string.
    ori_suffix=[]
    for i in range(len(ori_str)):
        temp_str=""
        for j in range(i,len(ori_str)):
            temp_str+=ori_str[j]
        ori_suffix.append(temp_str)

    # Generate all suffixes of the reverse string.
    rev_suffix=[]
    for i in range(len(rev_str)):
        temp_str=""
        for j in range(i,len(rev_str)):
            temp_str+=rev_str[j]
        rev_suffix.append(temp_str)

    # Add the suffix of the original string into the Trie. (a new Trie).
    root=TrieNode()

    for i in range(len(ori_suffix)):
        addOriSuffix(root,ori_suffix[i],i)

    # Add the suffix of the reverse string into the Trie. (the same Trie).
    for i in range(len(rev_suffix)):
        addRevSuffix(root,rev_suffix[i])

    # Now go through the Trie and retrieve the nodes that had its "matched" variable
    # set to True, because it means that the characters from the original suffix and reverse
    # suffix are intersecting. So, those nodes would be part of the substring that has a reverse
    # that exists in the original word.
    index_list=[]
    mylist=[]
    # Loop through all the original suffixes.
    for word in ori_suffix:
        node = root
        string=""
        counter=0
        # Loop through each character in the suffix.
        for char in word:
            index = getIndex(char)
            # In the event that the position is None, the list is returned,
            # but it would never go here because we're searching for the
            # words that we know we have inserted into the Trie earlier.
            if node.children[index] == None:
                return mylist

            # Given that the position is not empty, point the node to its child.
            node = node.children[index]

            # Previously, we have marked the nodes where the original suffix and reverse suffix
            # intersect, so here we check if it does. If it does intersect, we get the character
            # of that position and add it to a string.
            if node.match==True:
                if node.character!=None:
                    string+=node.character

            # Here, we will extract the nodes (character) if the last character of
            # that string has not been checked yet.
            if node.checked==False:
                if mylist==[]:
                    # Can't be just one character.
                    if len(string)>1:
                        mylist.append(string)
                        index_list.append((node.index_list))
                        counter+=1

                # Can't be just one character.
                if len(string)>1 :
                    if counter==0:

                        mylist.append(string)
                        index_list.append((node.index_list))
                        counter+=1

                    # If the previous item has the same length of the current item in this round of iteration
                    # of the outerloop, then it means that the word is repeated, so it is made sure that the
                    # repeated word is not added into the list.
                    elif len(string)!=len(mylist[-1]):

                        mylist.append(string)
                        index_list.append((node.index_list))

                # Once the string has been added to the list, the last character of that string is marked as
                # checked so that the same sequence of strings won't be checked for again.
                node.checked = True

    # Finally, get all the strings from mylist and its corresponding indexes from index_list, and format
    # them accordingly by putting them as a list of list into the final_list, before finally returning the
    # final_list.
    final_list=[]
    for index in range(len(index_list)):
        i=0
        while i<len(index_list[index]):
            final_list.append([mylist[index],index_list[index][i]])
            i+=1

    # Return the final_list.
    return(final_list)


def addOriSuffix(root,suffix,position_index):
    """
    This function adds suffixes into the Trie.
    Time complexity:  Best: O((K)
                      Worst: O((K)
    Space complexity:  Best: O(K)
                       Worst: O(K)
    Error handle: None.
    Return: None.
    Parameter: root, which is a reference to the TrieNode class; suffix which are all the suffixes
                of a given string, and position_index, which is the index of the suffixes.
    Precondition: the suffix parameter must be a suffix of the string.
    """

    # Point the node to the root.
    node=root

    # Add all the characters from the original suffix into the Trie.
    for char in suffix:
        # Get the index of the character.
        index = getIndex(char)
        # If the character doesn't exist, create a new Trie at that index.
        if node.children[index] == None:
            node.children[index] = TrieNode()

        # Point the node to its child.
        node = node.children[index]

        # Append the index of the character from the string into the nodes index_list.
        if node.index_list == []:
            node.index_list.append(position_index)

        # Ensure the same index is not repeated.
        elif node.index_list[-1] != position_index:
            node.index_list.append(position_index)

        # Set that nodes character to the current character.
        node.character = char

def addRevSuffix(root,suffix):
    """
    This function adds suffixes into the Trie.
    Time complexity:  Best: O((K)
                      Worst: O((K)
    Space complexity:  Best: O(K)
                       Worst: O(K)
    Error handle: None.
    Return: None.
    Parameter: root, which is a reference to the TrieNode class, and suffix which are all
                the suffixes of a given string.
    Precondition: the suffix parameter must be a suffix of the string.
    """

    # Point the node to the root.
    node = root

    # Put all the characters from the reverse suffix into the Trie.
    for char in suffix:
        # Get the index of the character.
        index = getIndex(char)
        # If the character doesn't exist, create a new Trie at that index.
        if node.children[index] == None:
            node.children[index] = TrieNode()

        # If character does exist, point to its child and mark it as match.
        # Marking it as matched would simply mean that this character in the reverse
        # substring has intersected with a character from the original list.
        if node.children[index] != None:
            node = node.children[index]
            # Mark true if they match.
            node.match = True
        # Set its character to the current character.
        node.character = char


# MAIN BLOCK
if __name__ == '__main__':

    LINES = "---------------------------------------------------------------------"
    print("TASK-1:")
    print(LINES)

    # Try input the filename and open it. If successful, continue to get id prefix input.
    bflag=False
    while bflag==False:
        try:
            database_file=input("Enter the file name of the query database : ")
            openTestfile = open(database_file, "r")
            bflag = True
        except NameError:
            bflag = False
        except TypeError:
            bflag = False
        except FileNotFoundError:
            bflag = False
        except IOError:
            bflag = False

    # Try input the id prefix. If successful, continue to get last name prefix input.
    bflag=False
    while bflag==False:
        try:
            prefix_id_input=input("Enter the prefix of the identification number: ")
            if prefix_id_input=="":
                bflag=True
            else:
                int(prefix_id_input)
                bflag=True
        except NameError:
            bflag = False
        except TypeError:
            bflag = False
        except ValueError:
            bflag = False
        except IOError:
            bflag = False

    # Try input the last name prefix. If successful, continue to run the query function.
    bflag=False
    while bflag==False:
        try:
            prefix_lastname_input=input("Enter the prefix of the last name : ")
            if prefix_lastname_input == "":
                bflag = True
            else:
                bflag=True
        except NameError:
            bflag = False
        except TypeError:
            bflag = False
        except ValueError:
            bflag = False
        except IOError:
            bflag = False


    mylist=(query(database_file,prefix_id_input,prefix_lastname_input))

    print(LINES)
    print(str(len(mylist))+" record found")
    for i in mylist:
        print("Index number : "+str(i))

    print(LINES)


    print("TASK-2:")
    # Try input the filename for reverse substring search. If successful, continue to run the function.
    bflag=False
    while bflag==False:
        try:
            file_input=input("Enter the file name for searching reverse substring: ")
            openTestfile = open(file_input, "r")
            bflag=True
        except NameError:
            bflag = False
        except TypeError:
            bflag = False
        except FileNotFoundError:
            bflag = False
        except IOError:
            bflag = False

    print(LINES)
    string=""
    result=(reverseSubstrings(file_input))

    # Displaying the result as depicted in the assignment spec sheet.
    for i in range(len(result)):
        string+=str(result[i][0])
        string+="{"
        string+=str(result[i][1])
        string+="}"
        if i<len(result)-1:
            string+=(",")
            string+=(" ")
    print(string)
    print(LINES)
    print("Program end")

# END OF ASSIGNMENT