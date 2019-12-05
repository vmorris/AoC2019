from itertools import permutations
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

class machine:
    def __init__(self):
        self.initial_load = []
        self.storage = []
        self.running = False
        self.ip = 0
    
    def load_from_csv(self, data):
        self.initial_load = list(map(int, data.rstrip().split(',')))
        self.reset()
    
    def reset(self):
        logging.debug('machine reset')
        self.storage = self.initial_load.copy()
    
    def step(self):
        logging.debug('step')
        self.execute(self.decode(self.fetch()))
    
    def run(self):
        logging.debug('run')
        self.running = True
        while self.running:
            self.step()            
        
    def halt(self):
        logging.debug('halt')
        self.running = False
        
    def fetch(self):
        logging.debug(f'fetch, ip={self.ip}, opcode={self.storage[self.ip]}')
        if self.storage[self.ip] == 99:
            self.ip += 1
            return [99]
        machine_code = self.storage[self.ip:self.ip+4]
        self.ip += 4
        return machine_code
    
    def decode(self, machine_code):
        logging.debug(f'decode, machine_code={machine_code}')
        return machine_code
        '''if code == 99:
            return code
        opcode = code[0]
        noun = code[1]
        verb = code[2]
        location = code[3]
        return [opcode, noun, verb, location]'''
        
    def execute(self, machine_code):
        if machine_code[0] == 99:
            self.halt()
        elif machine_code[0] == 1:
            self._add(machine_code[1], machine_code[2], machine_code[3])
        elif machine_code[0] == 2:
            self._mul(machine_code[1], machine_code[2], machine_code[3])

    def _add(self, noun, verb, location):
        logging.debug(f'add {self.storage[noun]},{self.storage[verb]}, location={location}')
        self.storage[location] = self.storage[noun] + self.storage[verb]
        
    def _mul(self, noun, verb, location):
        logging.debug(f'mul {self.storage[noun]},{self.storage[verb]}, location={location}')
        self.storage[location] = self.storage[noun] * self.storage[verb]

    def __repr__(self):
        return str(self.storage)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
        
    machine = machine()
    machine.load_from_csv(code)
    machine.run()
    print(machine)
    '''
    inputs = range(100)
    combos = permutations(inputs, r=2)
    
    for noun, verb in combos:
        machine = code.copy()
        machine[1] = noun
        machine[2] = verb
        i = 0
        step = 4
        while i < len(machine):
            opcode = machine[i:i+step]
            if opcode[0] == 99:
                break
            execute(opcode, machine)
            i += step
        if machine[0] == 19690720:
            print(100 * noun + verb)
   '''