const form = document.getElementById("loanForm");
const statusText = document.getElementById("status");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const application = {
        fullname: document.getElementById("fullname").value,
        phone: document.getElementById("phone").value,
        amount: document.getElementById("amount").value,
        period: document.getElementById("period").value,
        country: document.getElementById("country").value
    };

    statusText.textContent = "Submitting application...";

    try {
        const response = await fetch("/apply", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(application)
        });

        const result = await response.json();

        if (result.success) {
            statusText.textContent = "Application submitted successfully.";
            form.reset();
        } else {
            statusText.textContent = "Submission failed.";
        }

    } catch (error) {
        statusText.textContent = "Server connection error.";
        console.error(error);
    }
});
