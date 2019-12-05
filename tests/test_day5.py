from aoc import day5

code1 = '1,9,10,3,2,3,11,0,99,30,40,50'
code2 = '3,0,4,0,99'

def new_machine(code):
    machine = day5.machine()
    machine.load_from_csv(code)
    return machine

def test_create_machine():
    machine = day5.machine()
    assert type(machine) is day5.machine
    assert machine.initial_load == []
    assert machine.storage == []
    assert machine.running == False
    assert machine.ip == 0

def test_machine_load_from_csv():
    machine = new_machine(code1)
    assert machine.initial_load is not None
    assert machine.storage == machine.storage

def test_machine_reset():
    machine = new_machine(code1)
    machine.storage = []
    machine.reset()
    assert machine.initial_load is not None
    assert machine.storage == machine.storage
    
def test_machine_step():
    machine = new_machine(code1)
    #todo

def test_machine_run():
    pass

def test_machine_halt():
    pass

def test_machine_fetch():
    machine = new_machine(code1)
    bytecode = machine.fetch()
    assert bytecode == machine.storage[0:4]
    assert machine.ip == 4
    bytecode = machine.fetch()
    assert bytecode == machine.storage[4:8]
    assert machine.ip == 8
    bytecode = machine.fetch()  # halt
    assert bytecode == [machine.storage[8]]
    assert machine.ip == 9
    
def test_machine_fetch_and_halt():
    machine = new_machine('99')
    bytecode = machine.fetch()  # halt
    assert bytecode == [machine.storage[0]]
    assert machine.ip == 1

def test_machine_decode():
    machine = new_machine(code1)

def test_machine_execute_halt():
    pass

def test_machine_execute_add():
    pass

def test_machine_execute_mul():
    pass

def test_machine_case1():
    machine = day5.machine()
    machine.load_from_csv(code1)
    machine.run()
    assert machine.storage[0] == 3500
    
def test_machine_case2():
    machine = day5.machine()
    machine.load_from_csv(code2)
    machine.run()
