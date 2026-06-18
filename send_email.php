<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 1. Kusafisha data kutoka kwenye form
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject_form = strip_tags(trim($_POST["subject"]));
    $message = nl2br(htmlspecialchars(trim($_POST["message"])));

    // Validation ya haraka
    if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<script>alert('Please fill out the form correctly and provide a valid email address.'); window.history.back();</script>";
        exit;
    }

    // 2. Email yako ya kupokelea maombi
    $to = "info@kilimoratz.com";

    // 3. Subject ya email kwenye inbox yako
    $subject = "🌍 New Safari & Booking Inquiry: " . $subject_form;

    // 4. Muundo wa barua pepe (HTML Email Template)
    $email_content = '
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }
            .container { max-width: 600px; background: #ffffff; margin: 0 auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #27ae60; }
            .header { background: linear-gradient(135deg, #2c3e50, #27ae60); padding: 25px; text-align: center; color: white; }
            .header h1 { margin: 0; font-size: 22px; letter-spacing: 1px; }
            .header p { margin: 5px 0 0 0; opacity: 0.9; font-size: 14px; }
            .content { padding: 30px; }
            .info-table { width: 100%; border-collapse: collapse; margin-bottom: 25px; }
            .info-table td { padding: 10px 0; border-bottom: 1px solid #eee; }
            .info-table td.label { font-weight: bold; color: #666; width: 35%; }
            .info-table td.value { color: #222; }
            .message-box { background: #f9f9f9; border-left: 4px solid #27ae60; padding: 15px; border-radius: 4px; font-style: italic; line-height: 1.6; }
            .footer { background: #f4f7f6; text-align: center; padding: 15px; font-size: 12px; color: #777; border-top: 1px solid #eee; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🦁 Kilimora TZ Safari Inquiry</h1>
                <p>New Tour booking request received</p>
            </div>
            <div class="content">
                <table class="info-table">
                    <tr>
                        <td class="label">Client Name:</td>
                        <td class="value"><strong>' . $name . '</strong></td>
                    </tr>
                    <tr>
                        <td class="label">Email Address:</td>
                        <td class="value"><a href="mailto:' . $email . '">' . $email . '</a></td>
                    </tr>
                    <tr>
                        <td class="label">Interested Tour:</td>
                        <td class="value">' . $subject_form . '</td>
                    </tr>
                </table>
                
                <h3 style="color: #2c3e50; margin-bottom: 10px;">Safari Request Details:</h3>
                <div class="message-box">
                    ' . $message . '
                </div>
            </div>
            <div class="footer">
                <p>This email was automatically generated from the Booking Inquiry form on your website.</p>
                <p>&copy; ' . date("Y") . ' Kilimora TZ. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    ';

    // 5. Headers za HTML Email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: Kilimora Website <info@kilimoratz.com>" . "\r\n"; 
    $headers .= "Reply-To: " . $email . "\r\n"; 
    $headers .= "X-Mailer: PHP/" . phpversion();

    // 6. Kutuma email na Kumrudisha Localhost
    if (mail($to, $subject, $email_content, $headers)) {
        // Ujumbe mzuri wa Kiingereza kwa mteja + kurudi kwenye contact.html ya localhost
        echo "<script>
                alert('Thank you, " . $name . "! ✨ Your safari inquiry has been received successfully. Our tour experts are already working on your request, and we will get back to you within 24 hours. Karibu Tanzania! 🇹🇿');
                window.location.href='https://localhost/kilimora/contact.html'; 
              </script>";
        exit;
    } else {
        echo "<script>
                alert('Sorry, we could not process your request at the moment. Please try again.');
                window.history.back();
              </script>";
        exit;
    }
} else {
    header("Location: https://localhost/kilimora/contact.html");
    exit;
}
?>










<?php
// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     // 1. Sanitize and collect form data to protect against malicious inputs
//     $name = strip_tags(trim($_POST["name"]));
//     $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
//     $subject_form = strip_tags(trim($_POST["subject"]));
//     $message = trim($_POST["message"]);

//     // Simple validation to ensure fields are not empty and email is valid
//     if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
//         echo "<script>alert('Please fill out the form correctly.'); window.history.back();</script>";
//         exit;
//     }

//     // 2. Destination email address
//     $to = "info@kilimoratz.com";

//     // 3. Subject of the email that you will see in your inbox
//     $subject = "New Booking Inquiry: " . $subject_form;

//     // 4. Construct the email body/content
//     $email_content = "You have received a new inquiry from your website form:\n\n";
//     $email_content .= "Name: $name\n";
//     $email_content .= "Email: $email\n";
//     $email_content .= "Subject: $subject_form\n\n";
//     $email_content .= "Message:\n$message\n";

//     // 5. Email Headers (Prevents spam and structures the sender info)
//     // Always use an email from your own domain (like info@kilimoratz.com) as the 'From' address
//     $headers = "From: info@kilimoratz.com\r\n"; 
//     // This allows you to just click 'Reply' in your inbox to respond directly to the user
//     $headers .= "Reply-To: $email\r\n"; 
//     $headers .= "X-Mailer: PHP/" . phpversion();

//     // 6. Send the email
//     if (mail($to, $subject, $email_content, $headers)) {
//         // Success alert and redirect back to your home/form page (change index.html if needed)
//         echo "<script>alert('Thank you! Your message has been sent successfully.'); window.location.href='index.html';</script>"; 
//     } else {
//         // Failure alert
//         echo "<script>alert('Oops! Something went wrong and we couldn\'t send your message.'); window.history.back();</script>";
//     }
// } else {
//     // Redirect users if they try to access the PHP file directly
//     header("Location: index.html");
//     exit;
// }
?>




<!-- in swahili -->

<?php
// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     // 1. Kupokea data kutoka kwenye Form na kuzisafisha
//     $name = strip_tags(trim($_POST["name"]));
//     $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
//     $subject_form = strip_tags(trim($_POST["subject"]));
//     $message = trim($_POST["message"]);

//     // Kuhakikisha field zote zimejazwa
//     if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
//         echo "<script>alert('Tafadhali jaza fomu vizuri na uweke email sahihi.'); window.history.back();</script>";
//         exit;
//     }

//     // 2. Anwani ya Email yako inayopokea ujumbe
//     $to = "info@kilimoratz.com";

//     // 3. Kichwa cha Email kitakachoonekana kwenye inbox yako
//     $subject = "New Booking Inquiry: " . $subject_form;

//     // 4. Muundo wa Ujumbe wenyewe jinsi utakavyousoma
//     $email_content = "Umekatibu ujumbe mpya kutoka kwenye website yako:\n\n";
//     $email_content .= "Jina: $name\n";
//     $email_content .= "Email: $email\n";
//     $email_content .= "Subject: $subject_form\n\n";
//     $email_content .= "Ujumbe:\n$message\n";

//     // 5. Email Headers (Inasaidia isiende kwenye Spam na ionekane imetoka kwa nani)
//     $headers = "From: info@kilimoratz.com\r\n"; // Inashauriwa itoke kwenye email ya domain yako
//     $headers .= "Reply-To: $email\r\n"; // Ukiclick reply, iende kwa aliyetuma fomu
//     $headers .= "X-Mailer: PHP/" . phpversion();

//     // 6. Kutuma Email
//     if (mail($to, $subject, $email_content, $headers)) {
//         // Ujumbe ukienda vizuri, mtumiaji anarudishwa kwenye page ya nyuma au home
//         echo "<script>alert('Asante! Ujumbe wako umetumwa kikamilifu.'); window.location.href='index.html';</script>"; 
//         // Badilisha index.html kuwa jina la page yako ya fomu kama ni tofauti
//     } else {
//         echo "<script>alert('Samahani, kuna tatizo limetokea. Ujumbe haujatumwa.'); window.history.back();</script>";
//     }
// } else {
//     // Mtumiaji akijaribu kufungua faili hili moja kwa moja bila kujaza form
//     header("Location: index.html");
//     exit;
// }   
?>