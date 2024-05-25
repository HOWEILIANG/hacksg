$(document).ready(function () {
  $("#registrationForm").submit(function (event) {
    event.preventDefault();
    const firstName = $("#firstName").val();
    const lastName = $("#lastName").val();
    const email = $("#email").val();
    const password = $("#password").val();
    const confirmPassword = $("#confirmPassword").val();
    const terms = $("#terms").is(":checked");

    // Perform client-side validation
    if (
      firstName.trim() === "" ||
      lastName.trim() === "" ||
      email.trim() === "" ||
      password.trim() === "" ||
      confirmPassword.trim() === ""
    ) {
      alert("Please fill in all fields.");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    if (!terms) {
      alert("Please agree to the terms and conditions.");
      return;
    }

    // If all validations pass, you can proceed with form submission or other actions
    alert("Registration successful!");
    // Here you can send the form data to your backend for further processing
    // Redirect to index.html
    window.location.href = "index.html";
  });

  $(document).ready(function () {
    $("#passwordToggle").click(function () {
      var type = $("#pwd").attr("type") === "password" ? "text" : "password";
      $("#pwd").attr("type", type);
      $(this).text(type === "password" ? "Show" : "Hide");
    });

    $("#loginForm").submit(function (event) {
      event.preventDefault(); // Prevent default form submission

      var email = $("#email").val();
      var password = $("#pwd").val();

      // Basic client-side validation
      if (!email.trim() || !password.trim()) {
        $("#loginFeedback").text("Please enter both email and password.");
        return;
      }

      // Submit form data using AJAX
      $.ajax({
        type: "POST",
        url: $(this).attr("action"),
        data: $(this).serialize(),
        success: function (response) {
          // Handle successful login response
          // Redirect or show success message
        },
        error: function (xhr, status, error) {
          // Handle login error
          $("#loginFeedback").text(
            "Invalid email or password. Please try again."
          );
        },
      });
    });
  });
});
