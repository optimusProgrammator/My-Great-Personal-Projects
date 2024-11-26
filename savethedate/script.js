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
    const groupedEvents = events.reduce((acc, event) => {
      const month = new Date(event.date).toLocaleString("default", { month: "long" });
      if (!acc[month]) acc[month] = [];
      acc[month].push(event);
      return acc;
    }, {});

    for (const [month, monthEvents] of Object.entries(groupedEvents)) {
      const monthDiv = document.createElement("div");
      monthDiv.innerHTML = `<h3>${month}</h3>`;
      monthEvents.forEach(event => {
        const eventDiv = document.createElement("div");
        eventDiv.className = "event-card";
        eventDiv.innerHTML = `
          <strong>${event.eventName}</strong> (${event.eventType})<br>
          <em>${event.recipientName}</em><br>
          Date: ${new Date(event.date).toDateString()}
        `;
        monthDiv.appendChild(eventDiv);
      });
      eventList.appendChild(monthDiv);
    }
  };

  eventForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const eventName = document.getElementById("event-name").value;
    const recipientName = document.getElementById("recipient-name").value;
    const eventType = document.getElementById("event-type").value;
    const eventDate = document.getElementById("event-date").value;

    events.push({ eventName, recipientName, eventType, date: eventDate });
    saveEvents();
    eventForm.reset();
  });

  const checkNotifications = () => {
    const today = new Date();
    events.forEach(event => {
      const eventDate = new Date(event.date);
      const diffDays = Math.floor((eventDate - today) / (1000 * 60 * 60 * 24));
      if (diffDays >= 0 && diffDays <= 7) {
        alert(`Upcoming: ${event.eventName} on ${eventDate.toDateString()}`);
      }
    });
  };

  renderEvents();
  checkNotifications();
});
