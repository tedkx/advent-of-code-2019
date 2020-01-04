(function() {
  const paramConfig = {
    '0': null,
    '1': { count: 3, outputLast: true },
    '2': { count: 3, outputLast: true },
    '3': { count: 1, outputLast: true },
    '4': { count: 1, outputLast: false },
    '5': { count: 2, outputLast: false },
    '6': { count: 2, outputLast: false },
    '7': { count: 3, outputLast: true },
    '8': { count: 3, outputLast: true },
    '9': { count: 1, outputLast: false },
  };
  Object.keys(paramConfig).forEach(key => {
    if (!paramConfig[key]) return;
    paramConfig[key].arr = Array.from(Array(paramConfig[key].count)).map(
      () => 0
    );
  });

  const get = (lst, idx) => lst[idx] || 0;

  const iterate = (program, input) => {
    while (program.idx < program.lst.length) {
      const { lst, idx } = program;
      const raw = lst[idx] + '';
      const op = parseInt(raw.substr(raw.length - 2)) + '';
      if (op === '99') return { status: 'HALT' };
      const paramModes = paramConfig[op].arr.map(
        (_, i) => parseInt(raw[raw.length - 3 - i]) || 0
      );
      const params = paramConfig[op].arr.map(
        (_, i, arr) =>
          paramModes[i] === 1 &&
          !(i === arr.length - 1 && paramConfig[op].outputLast === true)
            ? idx + i + 1
            : get(lst, idx + i + 1) +
              (paramModes[i] === 2 ? program.relativeBase : 0)
      );

      //console.log(op, idx, paramModes, params);
      let output = null;

      if (op === '1')
        lst[params[2]] = get(lst, params[0]) + get(lst, params[1]);
      else if (op === '2')
        lst[params[2]] = get(lst, params[0]) * get(lst, params[1]);
      else if (op === '3') lst[params[0]] = input;
      else if (op === '4') output = get(lst, params[0]);
      else if (op === '5') {
        if (get(lst, params[0]) !== 0) {
          program.idx = get(lst, params[1]);
          continue;
        }
      } else if (op === '6') {
        if (get(lst, params[0]) === 0) {
          program.idx = get(lst, params[1]);
          continue;
        }
      } else if (op === '7')
        lst[params[2]] = get(lst, params[0]) < get(lst, params[1]) ? 1 : 0;
      else if (op === '8')
        lst[params[2]] = get(lst, params[0]) === get(lst, params[1]) ? 1 : 0;
      else if (op === '9') program.relativeBase += lst[params[0]];
      else return { status: 'INVALID INSTRUCTION' };

      program.idx += paramConfig[op].count + 1;

      if (output !== null) return { status: 'OUTPUT', payload: output };
    }

    return { status: 'END' };
  };

  const createProgram = inputStr => {
    const lst = inputStr.trim().split(',').map(num => parseInt(num));

    const program = {
      idx: 0,
      lst,
      outputs: [],
      phase: 0,
      relativeBase: 0,
      process: input => {
        const outputs = [];
        while (outputs.length < 2) {
          const { status, payload } = iterate(program, input);
          if (status === 'OUTPUT') outputs.push(payload);
          else break;
        }
        return outputs;
      },
    };
    return program;
  };

  window.createProgram = createProgram;
})();
