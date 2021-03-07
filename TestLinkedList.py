

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        links = 0
        position = self.first
        while position != None:
            links += 1
            position = position.next
        return links

    # add an item at the beginning of the list
    def insert_first(self, data):
        new = Link(data)
        new.next = self.first
        self.first = new

    # add an item at the end of a list
    def insert_last(self, data):
        new = Link(data)
        position = self.first
        if position == None:
            self.first = new
            return

        while position.next != None:
            position = position.next
        position.next = new
        new.next = None

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new = Link(data)
        previous = self.first
        if self.first == None:
            return
        position = previous.next
        if position == None:
            self.first = new
            return
        while position.next != None:
            if position.data <= data:
                position = position.next
                previous = previous.next
            else:
                new = previous.next
                position = new.next
                return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        position = self.first
        if position == None:
            return None
        while position.data != data:
            if position.next == None:
                return None
            else:
                position = position.next
        return position

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        position = self.first
        if position == None:
            return None
        while position.data != data:
            if position.next.data > data:
                return None
            elif position.next == None:
                return None
            else:
                position = position.next
        return position

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        position = self.first
        previous = self.first
        if position == None:
            return None
        while position.data != data:
            if position.next == None:
                return None
            else:
                previous = position
                position = position.next
        if position == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return position

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        position = self.first
        i = 0
        while position != None:
            if i % 10 == 0:
                print()
            print(position.data, end='  ')
            position = position.next
            i += 1

    # Copy the contents of a list and return new list
    def copy_list(self):
        new = LinkedList()
        position = self.first
        while position != None:
            new.insert_last(position.data)
            position = position.next
        return new

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        new = LinkedList()
        position = self.first
        while position != None:
            new .insert_first(position.data)
            position = position.next
        return new


    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        sorted = LinkedList()
        position = self.first
        while position != None:
            sorted.insert_in_order(position.data)
            position = position.next
        return sorted

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        position = self.first.next
        previous = self.first
        if previous == None:
            return False
        while position != None:
            if position.data < previous.data:
                return False
            else:
                position = position.next
                previous = previous.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def helper(self, other):
        merge = LinkedList()
        if self.get_num_links() == 0:
            return other.__str__()
        elif other.get_num_links() == 0:
            return self.__str__()
        else:
            merge.first = self.merge_list(self.first, other.first)
        return merge

    def merge_list(self, p, q):
        if p.data <= q.data:
            start = p
            p = p.next
        else:
            start = q
            q = q.next
        x = start
        while p != None and q != None:
            if p.data <= q.data:
                x.next = p
                p = p.next
            else:
                x.next = q
                q = q.next
            x = x.next
        while p != None:
            x.next = p
            p = p.next
            x = x.next
        while q != None:
            x.next = q
            q = q.next
            x = x.next
        return start

        # if only the other linked list still has links
        while q != None:
            new_list.insert_last(q.data)
            q = q.next

        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        one = self.first
        two = other.first

        # if one is empty and the other is not return False
        if one == None and two != None:
            return False
        elif one != None and two == None:
            return False

        # if both have links traverse and see if each is equal
        while one != None and two != None:
            if one.data != two.data:
                return False
            else:
                one = one.next
                two = two.next

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        l = []
        curr = self.first
        i = 0
        while curr != None:
            l.append(curr.data)
            curr = curr.next
            i += 1
        l = [i for n, i in enumerate(l) if i not in l[:n]]

        new = LinkedList()
        for i in l:
            new.insert_last(i)
        return new


def main():
# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.
    nums = LinkedList()
    edge = LinkedList()
    edge.insert_first(0)
    nums.insert_first(11)
    nums.insert_first(10)
    nums.insert_first(9)
    nums.insert_first(8)
    nums.insert_first(7)
    nums.insert_first(6)
    nums.insert_first(5)
    nums.insert_first(4)
    nums.insert_first(3)
    nums.insert_first(2)
    nums.insert_first(1)
# Test method insert_last()
    nums.insert_last(20)

# Test method insert_in_order()
    nums.insert_in_order(10)
    nums.insert_in_order(21)
    nums.insert_in_order(0)
    edge.insert_in_order(1)
    print(nums.__str__())

# Test method get_num_links()
    print(nums.get_num_links())
# Test method find_unordered()
# Consider two cases - data is there, data is not there
    unordered = LinkedList()
    unordered.insert_first(5)
    unordered.insert_last(3)
    unordered.insert_last(7)
    unordered.insert_last(1)
    print("hi")
    print(unordered.find_unordered(3))
    print(unordered.find_unordered(4))

# Test method find_ordered()
# Consider two cases - data is there, data is not there
    #print(nums.find_ordered(3))
    #print(nums.find_ordered(23))
# Test method delete_link()
# Consider two cases - data is there, data is not there
    nums.delete_link(21)
    nums.delete_link(50)

# Test method copy_list()
    copied = nums.copy_list()

# Test method reverse_list()
    rev = copied.reverse_list()
# Test method sort_list()
    in_order = unordered.sort_list()
# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted
    #print(in_order.is_sorted())
    #print(unordered.is_sorted())
    single = LinkedList()
    single.insert_last(5)
    print(single.is_sorted())

# Test method is_empty()
    empty = LinkedList()
    print(empty.is_empty())
    print(single.is_empty())
    print(nums.is_empty())

# Test method merge_list()
    #merged = nums.merge_list(unordered)
    #print(merged)
# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal
    print(nums.is_equal(copied))
    print(nums.is_equal(unordered))
    print(nums.is_equal(empty))
# Test remove_duplicates()
    no_duplicates = nums.remove_duplicates()
if __name__ == "__main__":
    main()
