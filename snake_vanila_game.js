const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const highScoreEl = document.getElementById('high-score');
const messageEl = document.getElementById('message');
const startBtn = document.getElementById('startBtn');
const speedSlider = document.getElementById('speed');
const speedLabel = document.getElementById('speed-label');

const GRID = 20;
const COLS = canvas.width / GRID;
const ROWS = canvas.height / GRID;

const FRUITS = ['🍌', '🥭', '🍇', '🍈', '🫐'];

const SPEED_MAP = { 1: { ms: 200, label: 'Slow' }, 2: { ms: 160, label: 'Easy' }, 3: { ms: 120, label: 'Normal' }, 4: { ms: 80, label: 'Fast' }, 5: { ms: 50, label: 'Insane' } };

let snake, direction, nextDirection, food, score, highScore, gameLoop, running, speed;

highScore = localStorage.getItem('rfSnakeHigh') || 0;
highScoreEl.textContent = highScore;

function init() {
    snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
    direction = { x: 1, y: 0 };
    nextDirection = { x: 1, y: 0 };
    score = 0;
    scoreEl.textContent = score;
    placeFood();
    messageEl.textContent = '';
    running = true;
    speed = parseInt(speedSlider.value);
    if (gameLoop) clearInterval(gameLoop);
    gameLoop = setInterval(update, SPEED_MAP[speed].ms);
}

function placeFood() {
    let pos;
    do {
        pos = { x: Math.floor(Math.random() * COLS), y: Math.floor(Math.random() * ROWS) };
    } while (snake.some(s => s.x === pos.x && s.y === pos.y));
    food = { ...pos, emoji: FRUITS[Math.floor(Math.random() * FRUITS.length)] };
}

function update() {
    direction = nextDirection;
    const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

    // Wall collision
    if (head.x < 0 || head.x >= COLS || head.y < 0 || head.y >= ROWS) return gameOver();
    // Self collision
    if (snake.some(s => s.x === head.x && s.y === head.y)) return gameOver();

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        score++;
        scoreEl.textContent = score;
        if (score > highScore) {
            highScore = score;
            highScoreEl.textContent = highScore;
            localStorage.setItem('rfSnakeHigh', highScore);
        }
        placeFood();
    } else {
        snake.pop();
    }

    draw();
}

function draw() {
    // Background with subtle leaf pattern
    ctx.fillStyle = '#1b3d1b';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw grid lines subtly
    ctx.strokeStyle = 'rgba(255,255,255,0.03)';
    for (let i = 0; i < COLS; i++) {
        for (let j = 0; j < ROWS; j++) {
            ctx.strokeRect(i * GRID, j * GRID, GRID, GRID);
        }
    }

    // Draw snake
    snake.forEach((seg, i) => {
        const brightness = Math.max(80, 180 - i * 5);
        ctx.fillStyle = i === 0 ? '#66bb6a' : `rgb(30, ${brightness}, 30)`;
        ctx.shadowColor = i === 0 ? '#a5d6a7' : 'transparent';
        ctx.shadowBlur = i === 0 ? 6 : 0;
        ctx.beginPath();
        ctx.roundRect(seg.x * GRID + 1, seg.y * GRID + 1, GRID - 2, GRID - 2, 4);
        ctx.fill();
        ctx.shadowBlur = 0;

        // Eyes on head
        if (i === 0) {
            ctx.fillStyle = '#fff';
            const ex = seg.x * GRID + (direction.x === 1 ? 13 : direction.x === -1 ? 4 : 6);
            const ey = seg.y * GRID + (direction.y === 1 ? 13 : direction.y === -1 ? 4 : 6);
            ctx.beginPath();
            ctx.arc(ex, ey, 2.5, 0, Math.PI * 2);
            ctx.arc(ex + (direction.y !== 0 ? 6 : 0), ey + (direction.x !== 0 ? 0 : 6), 2.5, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    // Draw food
    ctx.font = '16px serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(food.emoji, food.x * GRID + GRID / 2, food.y * GRID + GRID / 2);
}

function gameOver() {
    running = false;
    clearInterval(gameLoop);
    messageEl.textContent = `💀 Game Over! Score: ${score}. Press Start to play again.`;
}

// Controls
document.addEventListener('keydown', e => {
    if (!running && ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
        init();
        return;
    }
    switch (e.key) {
        case 'ArrowUp':    if (direction.y === 0) nextDirection = { x: 0, y: -1 }; break;
        case 'ArrowDown':  if (direction.y === 0) nextDirection = { x: 0, y: 1 }; break;
        case 'ArrowLeft':  if (direction.x === 0) nextDirection = { x: -1, y: 0 }; break;
        case 'ArrowRight': if (direction.x === 0) nextDirection = { x: 1, y: 0 }; break;
    }
});

startBtn.addEventListener('click', init);

speedSlider.addEventListener('input', () => {
    const val = parseInt(speedSlider.value);
    speedLabel.textContent = SPEED_MAP[val].label;
    if (running) {
        clearInterval(gameLoop);
        gameLoop = setInterval(update, SPEED_MAP[val].ms);
    }
});

// Initial draw
draw();
