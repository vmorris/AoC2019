from collections import namedtuple
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

ParameterMode = namedtuple('ParameterMode', ['parameter', 'mode'])

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
        opcode, params = self.decode(self.fetch())
        self.execute(opcode, params)
    
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
        instruction = self.storage[self.ip]
        opcode = instruction % 100
        if opcode == 99:
            machine_code = [99]
            self.ip += 1
        elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            machine_code = self.storage[self.ip:self.ip+4]
            self.ip += 4
        elif opcode == 3 or opcode == 4:
            machine_code = self.storage[self.ip:self.ip+2]
            self.ip += 2
        elif opcode == 5 or opcode == 6:
            machine_code = self.storage[self.ip:self.ip+3]
            self.ip += 3
        return machine_code
    
    def decode(self, machine_code):
        logging.debug(f'decode, machine_code={machine_code}')
        instruction = machine_code[0]
        opcode = instruction % 100
        parameter_modes = str(instruction // 100)
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            modes = parameter_modes.zfill(3)[::-1]  # padded and reversed
            params = []
            for i in range(3):
                params.append(ParameterMode(machine_code[i+1], int(modes[i])))
        elif opcode == 3 or opcode == 4:
            params = [ParameterMode(machine_code[1], int(parameter_modes[0]))]
        elif opcode == 5 or opcode == 6:
            modes = parameter_modes.zfill(2)[::-1]  # padded and reversed
            params = []
            for i in range(2):
                params.append(ParameterMode(machine_code[i+1], int(modes[i])))
        elif opcode == 99:
            params = None
        return opcode, params
        
    def execute(self, opcode, params):
        if opcode == 99:
            self.halt()
        elif opcode == 1:
            self._add(params)
        elif opcode == 2:
            self._mul(params)
        elif opcode == 3:
            self._input(params)
        elif opcode == 4:
            self._output(params)
        elif opcode == 5:
            self._jump_if_true(params)
        elif opcode == 6:
            self._jump_if_false(params)
        elif opcode == 7:
            self._less_than(params)
        elif opcode == 8:
            self._equals(params)

    def _add(self, params):
        logging.debug(f'add {params}')
        noun = params[0]
        verb = params[1]
        loc = params[2]
        if noun.mode == 0:
            _noun = self.storage[noun.parameter]
        elif noun.mode == 1:
            _noun = noun.parameter
        if verb.mode == 0:
            _verb = self.storage[verb.parameter]
        elif verb.mode == 1:
            _verb = verb.parameter
        self.storage[loc.parameter] = _noun + _verb
        
    def _mul(self, params):
        logging.debug(f'mul {params}')
        noun = params[0]
        verb = params[1]
        loc = params[2]
        if noun.mode == 0:
            _noun = self.storage[noun.parameter]
        elif noun.mode == 1:
            _noun = noun.parameter
        if verb.mode == 0:
            _verb = self.storage[verb.parameter]
        elif verb.mode == 1:
            _verb = verb.parameter
        self.storage[loc.parameter] = _noun * _verb

    def _input(self, params):
        logging.debug(f'input {params}')
        loc = params[0]
        self.storage[loc.parameter] = int(input())
        
    def _output(self, params):
        logging.debug(f'output {params}')
        loc = params[0]
        print(self.storage[loc.parameter])

    def _jump_if_true(self, params):
        logging.debug(f'jump_if_true {params}')
        test = params[0]
        jump = params[1]
        if test.mode == 0:
            _test = self.storage[test.parameter]
        else:
            _test = test.parameter
        if jump.mode == 0:
            _jump = self.storage[jump.parameter]
        else:
            _jump = jump.parameter
        if _test != 0:
            self.ip = _jump
    
    def _jump_if_false(self, params):
        logging.debug(f'jump_if_false {params}')
        test = params[0]
        jump = params[1]
        if test.mode == 0:
            _test = self.storage[test.parameter]
        else:
            _test = test.parameter
        if jump.mode == 0:
            _jump = self.storage[jump.parameter]
        else:
            _jump = jump.parameter
        if _test == 0:
            self.ip = _jump
        
    def _less_than(self, params):
        logging.debug(f'less_than {params}')
        noun = params[0]
        verb = params[1]
        loc = params[2]
        if noun.mode == 0:
            _noun = self.storage[noun.parameter]
        elif noun.mode == 1:
            _noun = noun.parameter
        if verb.mode == 0:
            _verb = self.storage[verb.parameter]
        elif verb.mode == 1:
            _verb = verb.parameter
        if _noun < _verb:
            self.storage[loc.parameter] = 1
        else:
            self.storage[loc.parameter] = 0
    
    def _equals(self, params):
        logging.debug(f'equals {params}')
        noun = params[0]
        verb = params[1]
        loc = params[2]
        if noun.mode == 0:
            _noun = self.storage[noun.parameter]
        elif noun.mode == 1:
            _noun = noun.parameter
        if verb.mode == 0:
            _verb = self.storage[verb.parameter]
        elif verb.mode == 1:
            _verb = verb.parameter
        if _noun == _verb:
            self.storage[loc.parameter] = 1
        else:
            self.storage[loc.parameter] = 0

    def __repr__(self):
        return str(self.storage)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = f.read().rstrip()
    
    #data = '1,9,10,3,2,3,11,0,99,30,40,50'
    #data = '3,0,4,0,99'
    #data = '1002,4,3,4,33'
    #data = '1101,100,-1,4,0'
    #data = '3,9,8,9,10,9,4,9,99,-1,8'

    m = machine()
    m.load_from_csv(data)
    m.run()
    