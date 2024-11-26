document.addEventListener("DOMContentLoaded", () => {
  const eventForm = document.getElementById("event-form");
  const eventList = document.getElementById("event-list");

  // Load events from localStorage
  let events = JSON.parse(localStorage.getItem("events")) || [];

  const saveEvents = () => {
    localStorage.setItem("events", JSON.stringify(events));
    renderEvents();
  };

  const renderEvents = () => {
    eventList.innerHTML = "";
    events.forEach((event, index) => {
      const eventDiv = document.createElement("div");
      eventDiv.className = "event-card";
      eventDiv.innerHTML = `
        <div>
          <strong>${event.eventName}</strong> (${event.eventType})<br>
          <em>${event.recipientName}</em><br>
          Date: ${event.month}/${event.day}/${event.year}<br>
          Frequency: ${event.frequency}
        </div>
        <button class="delete-btn" data-index="${index}">Delete</button>
      `;
      eventList.appendChild(eventDiv);
    });

    document.querySelectorAll(".delete-btn").forEach(button => {
      button.addEventListener("click", () => {
        const index = button.getAttribute("data-index");
        events.splice(index, 1);
        saveEvents();
      });
    });
  };

  eventForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const eventName = document.getElementById("event-name").value;
    const recipientName = document.getElementById("recipient-name").value;
    const eventType = document.getElementById("event-type").value;
    const eventMonth = document.getElementById("event-month").value;
    const eventDay = document.getElementById("event-day").value;
    const eventYear = document.getElementById("event-year").value;
    const eventFrequency = document.getElementById("event-frequency").value;

    events.push({
      eventName,
      recipientName,
      eventType,
      month: eventMonth,
      day: eventDay,
      year: eventYear,
      frequency: eventFrequency,
    });

    saveEvents();
    eventForm.reset();
  });

  renderEvents();
});
