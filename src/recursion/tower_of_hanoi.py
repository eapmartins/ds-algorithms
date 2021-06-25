def _tower_of_hanoi_helper(num_disks, source, aux, destination):
    if num_disks == 0:
        return

    if num_disks == 1:
        print("move from {} to {}".format(source, destination))
        return

    _tower_of_hanoi_helper(num_disks -1, source, destination, aux)
    print("move from {} to {}".format(source, destination))
    _tower_of_hanoi_helper(num_disks -1, aux, source, destination)

def tower_of_hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    _tower_of_hanoi_helper(num_disks, 'S', 'A', 'D')
    
tower_of_hanoi(3)
