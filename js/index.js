"use strict";

// Random Number generator
function randomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const $tinderContainer = $(".tinder");
let allCards = $(".tinder--card");
const $nope = $("#nope");
const $love = $("#love");
let num = 5;

// Initialize cards
function initCards() {
  const $newCards = $(".tinder--card:not(.removed)");

  $newCards.each(function (index) {
    $(this).css({
      zIndex: $newCards.length - index,
      transform: `translateY(-${index * 20}px)`,
    });
  });

  $tinderContainer.addClass("loaded");
}

// Convert node to string
function nodeToString(node) {
  const $tmpNode = $("<div></div>").append($(node).clone());
  return $tmpNode
    .html()
    .replace(/(\r\n|\n|\r)/gm, "")
    .replace(" removed", "");
}

// Clean and add new card
function addNewCard(thisCard) {
  const cleanedCard = nodeToString(thisCard);
  num++;
  const $allCardsArea = $(".tinder--cards");

  setTimeout(() => {
    $allCardsArea.append(cleanedCard);
    $(".removed").remove();
    initCards();
    addHammers();
  }, 300);
}

// Initialize Hammer.js on each card
function addHammers() {
  allCards = $(".tinder--card");

  allCards.each(function () {
    const hammertime = new Hammer(this);

    hammertime.on("pan", (event) => {
      $(this).addClass("moving");
      if (event.deltaX === 0) return;

      $tinderContainer.toggleClass("tinder_love", event.deltaX > 0);
      $tinderContainer.toggleClass("tinder_nope", event.deltaX < 0);

      const rotate = event.deltaX * 0.03;

      $(event.target).css(
        "transform",
        `translate(${event.deltaX}px) rotate(${rotate}deg)`
      );
    });

    hammertime.on("panend", (event) => {
      $(this).removeClass("moving");
      $tinderContainer.removeClass("tinder_love tinder_nope");

      const keep =
        Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

      if (keep) {
        $(event.target).css("transform", "");
      } else {
        const endX = Math.max(
          Math.abs(event.velocityX) * $("body").width(),
          $("body").width()
        );
        const toX = event.deltaX > 0 ? endX : -endX;
        const rotate = event.deltaX * 0.03;

        $(event.target).css(
          "transform",
          `translate(${toX}px) rotate(${rotate}deg)`
        );
        $(event.target).addClass("removed");

        addNewCard(event.target);
      }
    });
  });
}

// Create button listener
function createButtonListener(love) {
  return (event) => {
    const $cards = $(".tinder--card:not(.removed)");
    if (!$cards.length) return false;

    const $card = $cards.first();
    const moveOutWidth = $("body").width() * 1.5;

    $card.addClass("removed");

    if (love) {
      $card.css(
        "transform",
        `translate(${moveOutWidth}px, -100px) rotate(-30deg)`
      );
    } else {
      $card.css(
        "transform",
        `translate(-${moveOutWidth}px, -100px) rotate(30deg)`
      );
    }

    addNewCard($card[0]);
    event.preventDefault();
  };
}

const nopeListener = createButtonListener(false);
const loveListener = createButtonListener(true);

$nope.on("click", nopeListener);
$love.on("click", loveListener);

$(".closeMe").on("click", () => toggleInfoClose(true));
$(".covering").on("click", () => toggleInfoClose(true));
$("#info").on("click", () => toggleInfoClose(false));

function toggleInfoClose(bool) {
  if (!bool) {
    $(".tinder--info").css("top", "50%");
  } else {
    $(".tinder--info").css("top", "200vh");
  }
}

let fadein = null;

const myFunction = (fadeOutTime, fadeInAfterTime) => {
  $(".promptBox")
    .css("transition", fadeOutTime + "ms")
    .css("opacity", "0");

  if (fadein) {
    clearTimeout(fadein);
  }
  fadein = setTimeout(showMe, fadeInAfterTime);
};

const showMe = () => {
  $(".promptBox").css("opacity", "1");
};

$("body").on("mousemove click touchstart touchmove", () =>
  myFunction(300, 15000)
);

// Initialize the cards on page load
$(document).ready(() => {
  initCards();
  addHammers();
});

$(document).ready(function () {
  // Select the range input element by its ID
  var $rangeInput = $("#comfort-amount");
  // Select the output element
  var $output = $("#comfort-amount-output");

  // Update the displayed value when the range input changes
  $rangeInput.on("input", function () {
    $output.text("$" + $(this).val() + " (Monthly)");
  });
});

$(document).ready(function () {
  // Simulate fetching data from the server or previous page
  const financialData = {
    totalReturn: "35%",
    annualReturn: "12%",
    dividendYield: "1.2%",
    allocation: {
      stocks: 60,
      bonds: 30,
      cash: 10,
    },
  };

  // Populate the data in the cards
  $("#totalReturn").text(financialData.totalReturn);
  $("#annualReturn").text(financialData.annualReturn);
  $("#dividendYield").text(financialData.dividendYield);

  // Create the investment allocation chart
  const ctx = $("#allocationChart")[0].getContext("2d");
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Stocks", "Bonds", "Cash"],
      datasets: [
        {
          data: [
            financialData.allocation.stocks,
            financialData.allocation.bonds,
            financialData.allocation.cash,
          ],
          backgroundColor: ["#007bff", "#28a745", "#ffc107"],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              const label = context.label || "";
              const value = context.raw || 0;
              return `${label}: ${value}%`;
            },
          },
        },
      },
    },
  });
});
