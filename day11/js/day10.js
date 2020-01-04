(function() {
  directions = [ [ 0, -1 ], [ 1, 0 ], [ 0, 1 ], [ -1, 0 ] ];

  window.createRobot = () => {
    const robot = {
      move: arg => {
        robot.directionIdx += arg === 0 ? -1 : 1;
        if (robot.directionIdx >= directions.length) robot.directionIdx = 0;
        else if (robot.directionIdx < 0)
          robot.directionIdx = directions.length - 1;

        const [ x, y ] = robot.position;
        const [ dx, dy ] = directions[robot.directionIdx];
        robot.position = [ x + dx, y + dy ];
      },
      position: [ 0, 0 ],
      directionIdx: 0,
    };
    return robot;
  };

  const createKey = point => `${point[0]},${point[1]}`;

  window.createHull = () => {
    const hull = {
      getColor: point => {
        const key = createKey(point);
        return typeof hull.grid[key] === 'number' ? hull.grid[key] : 0;
      },
      grid: {},
      paint: (point, color) => {
        hull.grid[createKey(point)] = color;
      },
    };

    return hull;
  };
})();
