"use strict";

let controllerIndex = null;

//Implementing Event Listeners

window.addEventListener("gamepadconnected", (event) => {
  const gamepad = event.gamepad;
  controllerIndex = gamepad.index;
  console.log("connected");
});

window.addEventListener("gamepaddisconnected", (event) => {
  controllerIndex = null;
  console.log("disconnected");
});

//Handling Input
function handleButtons(buttons) {
  for (let i = 0; i < buttons.length; i++) {
    const button = buttons[i];
    const buttonElement = document.getElementById(`controller-b${i}`);
    const selectedButtonClass = "selected-button";

    if (buttonElement) {
      if (button.value > 0) {
        buttonElement.classList.add(selectedButtonClass);
        buttonElement.style.filter = `contrast(${button.value * 150}%)`;
      } else {
        buttonElement.classList.remove(selectedButtonClass);
        buttonElement.style.filter = `contrast(100%)`;
      }
    }
  }
}

function updateStick(elementId, leftRightAxis, upDownAxis) {
  const multiplier = 25;
  const stickLeftRight = leftRightAxis * multiplier;
  const stickUpDown = upDownAxis * multiplier;

  const stick = document.getElementById(elementId);

  const x = Number(stick.dataset.originalXPosition);
  const y = Number(stick.dataset.originalYPosition);

  stick.setAttribute("cx", x + stickLeftRight);
  stick.setAttribute("cy", y + stickUpDown);
}

function handleSticks(axes) {
  updateStick("controller-b10", axes[0], axes[1]);
  updateStick("controller-b11", axes[2], axes[3]);

  sendData(axes[2], axes[1]);
}

//Sending POST request

function sendData(LRAxisRj, UDAxisLj) {
  $.ajax({
    url: "/process",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      leftJoystickUD: UDAxisLj,
      rightJoystickLR: LRAxisRj,
    }),
    success: function (response) {
      console.log(response.result);
    },
    error: function (error) {
      console.log(`Error: ${error}`);
    },
  });
}
//Throttle Function

const throttle = (fn,delay)=>{
  let lastTime = 0;
  console.log('Throttling');
  return (...args) => {
    const now = new Date().getTime();
    if( now - lastTime < delay){
      return;
    }
    lastTime = now;
    fn(...args);
  }
}

const tHandleButtons = throttle(handleButtons,100);
const tHandleSticks = throttle(handleSticks,100);

function gameLoop() {
  if (controllerIndex !== null) {
    const gamepad = navigator.getGamepads()[controllerIndex];
    tHandleButtons(gamepad.buttons);
    tHandleSticks(gamepad.axes);
  }
  requestAnimationFrame(gameLoop);
}

gameLoop();

