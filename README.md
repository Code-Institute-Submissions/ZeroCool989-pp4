# DailyFinancePulse-

## Introduction

I'm thrilled to introduce **"Daily Finance Pulse"**, an online platform I've developed that's tailored for finance enthusiasts like me. It's designed to provide real-time financial news, insights, and analysis, catering to a diverse audience, including web developers and designers who have a keen interest in the world of finance.

### Agile Project Management

Throughout the development of **"Daily Finance Pulse,"** I adhered to Agile management principles, prioritizing flexibility, collaboration, and iterative progress. To effectively manage the project, I relied on a **Kanban board** https://github.com/users/ZeroCool989/projects/7, a visual tool that played a pivotal role in organizing and tracking our tasks.

### Kanban Board for Streamlined Project Management

**Task Organization:** The Kanban board served as the central hub for managing tasks. It allowed me to visualize our workflow, categorize tasks into columns such as *'To Do,' 'In Progress,'* and *'Done,'* and closely monitor the progress of each task as it transitioned through these stages.

**Adaptability and Prioritization:** The flexible nature of the Kanban board enabled me to adapt to changing requirements with ease. I could promptly reprioritize tasks to ensure that critical components received immediate attention.

### Agile Tools and Practices

In addition to the Kanban board, I adhered to other Agile principles and practices during the development of **"Daily Finance Pulse"**:

- **Iterative Development:** I embraced an iterative approach, continuously building and testing features to ensure they aligned with the evolving needs of  users. This methodology allowed me to deliver a robust and user-friendly platform.

- **User-Centric Approach:** I placed a strong emphasis on understanding and addressing user needs. By staying attuned to user preferences and feedback, I aimed to provide a tailored and valuable experience for our audience.


## Responsiveness Check Using Google Chrome Developer Tools

During the development and testing of my Django project, "Daily Finance Pulse," I conducted extensive checks for responsiveness using Google Chrome's Developer Tools. This was a crucial part of my process to ensure the application provided a consistent and user-friendly experience across different devices.

### Key Highlights of My Responsiveness Testing:

#### Laptop Devices:

- On laptop devices, the application's layout, typography, and interactive elements scaled well, offering an intuitive user experience.
- ![image](https://github.com/ZeroCool989/DailyFinancePulse-/assets/75548207/8f38e1aa-44d7-4917-87d2-4a7b90ce21ec)



#### Tablet Devices:

- I tested the application on various tablet screen sizes using the emulation feature in Chrome Developer Tools. The responsive design adapted smoothly, maintaining optimal display of content, images, and navigation.
- ![image](https://github.com/ZeroCool989/DailyFinancePulse-/assets/75548207/a77b4374-f75e-4779-8747-a9d2f8f151e0)


#### Mobile Devices:

- Recognizing the importance of mobile accessibility, I paid special attention to mobile responsiveness. My tests across multiple simulated mobile devices showed that the application's interface was highly adaptable. Elements like the navigation menu, post listings, and features such as commenting and liking were easily accessible and user-friendly.
- ![image](https://github.com/ZeroCool989/DailyFinancePulse-/assets/75548207/f84af1db-18cf-4fef-a687-e65b2014cade)


## UX 

##Color Palette

I understand the vital role that our color palette plays in shaping the user experience (UX) of our project. I've carefully chosen each color to evoke specific emotions and enhance the overall visual appeal of the platform.

### 1. Platinum (#E5E4E2)

![Platinum](https://via.placeholder.com/100/E5E4E2/000000?text=+)

**Platinum** is the primary text color and is used for branding elements. It conveys a sense of sophistication and professionalism, ensuring that text is easily readable and authoritative.

### 2. Muted Lime Green (#98C379)

![Muted Lime Green](https://via.placeholder.com/100/98C379/000000?text=+)

I've chosen **Muted Lime Green** as our accent color. It adds vibrancy and energy to interactive elements, buttons, and links, all of which are essential for encouraging user engagement and interaction.

### 3. Soft White (#F5F5F5)

![Soft White](https://via.placeholder.com/100/F5F5F5/000000?text=+)

**Soft White** serves as a choice for light backgrounds. It provides a clean and comfortable reading environment, creating a sense of spaciousness and ensuring that content is easily accessible.

### 4. Midnight Blue (#191970)

![Midnight Blue](https://via.placeholder.com/100/191970/000000?text=+)

For dark backgrounds, the masthead, and the footer, I've opted for **Midnight Blue**. It adds depth and contrast, making certain elements stand out and creating a visually appealing experience.

### 5. Pale Blue (#D3E5F5)

![Pale Blue](https://via.placeholder.com/100/D3E5F5/000000?text=+)

**Pale Blue** is my choice for the main background. It adds a calming and serene touch to the platform, ensuring a pleasant overall ambiance.

I've carefully curated this color palette to enhance the user experience, making the platform visually engaging, easy to navigate, and memorable. These colors work harmoniously to create a cohesive and inviting environment for our users.

## Typography

In our project, I believe that typography plays a pivotal role in crafting a visually engaging and reader-friendly design. I've taken special care to select fonts that not only enhance readability but also convey a sense of style and uniqueness:

### 1. Lato

![Lato Font](https://via.placeholder.com/100/000000/FFFFFF?text=Lato)

**Lato** serves as my primary font choice. It's a bold sans-serif typeface with a font-weight of 700. I chose Lato because it strikes a balance between professionalism and modernity, ensuring that text remains clear and authoritative. You'll find this font used for branding elements and throughout the main content of the platform.

### 2. Custom Fonts

In addition to Lato, I've introduced custom fonts strategically to infuse a distinctive personality into specific elements within our project. These custom fonts are carefully curated to enhance the overall aesthetics and establish a unique visual identity.

### 3. Thin Font Weight

For select text elements that require emphasis, I've employed a thin font weight with a font-weight of 300. This thin weight adds an extra layer of sophistication and distinctiveness to key textual components.

My typography choices are aimed at creating a cohesive and visually pleasing reading experience across the platform. I believe that these font selections contribute to readability while infusing a sense of style that sets our project apart.

## Features

### 1. User Authentication
- Users can register and create accounts.
- Users can log in and log out.
- Customized login and registration templates.

### 2. Blog Posts
- Display a list of blog posts on the homepage.
- Display individual blog posts with titles, authors, creation dates, and content.
- Each blog post can have a featured image.
- Users can like blog posts, and the like count is updated in real-time using AJAX.
- Users can leave comments on blog posts.
- Comments are paginated, and users can load more comments.
- Comments require approval before being displayed if the user is not authenticated.

### 3. Stylish Design
- Responsive design using Bootstrap for a seamless viewing experience on different devices.
- Custom fonts and icons for an appealing visual appearance.
- Bootstrap cards for displaying blog posts with images and metadata.
- Navigation bar for easy access to different sections of the website.

### 4. Cloudinary Integration
- Integration with Cloudinary for storing and serving images.
- Cloudinary used for the website's logo and featured images.

### 5. Messages
- Display alert messages for user feedback and notifications.
- Automatically close alert messages after 3 seconds.

### 6. Static Files and Media
- Management of static files (CSS, JavaScript, etc.) and media files (images, videos, etc.).
- Configuration for serving static files using Whitenoise.

### 7. Database
- Configuration for database using the `DATABASE_URL` environment variable.
- Uses PostgreSQL database, which is commonly used in production environments.

### 8. Social Network Links
- Display links to the developer's social network profiles in the website's footer.
- Links to LinkedIn, Xing, and GitHub profiles.

### 9. Security
- Implementation of security measures, such as setting `X_FRAME_OPTIONS` to 'SAMEORIGIN'.
- Use of environment variables to store sensitive information like secret keys and API credentials.

### 10. Django Features
- Utilizes Django's authentication system for user management.
- Implements Django's templating system for rendering dynamic HTML templates.
- Utilizes Django's messages framework for user notifications.
- Configuration of Django middleware for security and functionality.

### Packages Used
- Django: The web framework used for building the project.
- dj-database-url: For parsing database configuration from the `DATABASE_URL` environment variable.
- cloudinary-storage: Integration with Cloudinary for image storage.
- crispy-forms: For rendering forms with Bootstrap styles.
- django-summernote: Used for a rich text editor in blog post content.
- Whitenoise: For serving static files in production.
- psycopg2: PostgreSQL adapter for Django.
- Allauth: For user authentication and account management.
- Bootstrap: Front-end framework for responsive design.
- Font Awesome: For icons used in the project.
- jQuery: JavaScript library for AJAX functionality.
- Google Fonts: Custom fonts for the project.

## Testing

### Manual Testing
Throughout the development process, extensive manual testing was conducted to ensure the reliability and functionality of the DailyFinancePulse project. This testing included:
- Continuously checking and using the website's features during development.


### User Testing

- **Account Registration**: I tested registering accounts using various usernames.
- **Resource Submission**: I submited resources to identify any issues in the submission process.
- **Account Deletion**: Testing involved the deletion of user accounts.

User testing helped in catching potential issues from different user perspectives and ensuring that the website's functionality is user-friendly and reliable.

### Continuous Integration Testing
Continuous Integration (CI) testing was set up to automatically run tests and checks on code changes before they were merged into the main codebase. This CI process helped identify any regressions or issues introduced during development, ensuring that new features or changes did not break existing functionality.

### Browser Compatibility Testing
The project was tested on various web browsers, including but not limited to Chrome, Firefox, to ensure cross-browser compatibility and a consistent user experience.



# Code Validation

## HTML Validation (W3 HTML Validator)

During the HTML validation process, it's important to note that I encountered some error messages. These messages primarily stemmed from the use of Bootstrap elements and attributes within the project. Bootstrap, a widely adopted front-end framework, may trigger validation messages due to non-standard HTML attributes used to enhance styling and interactivity. I want to emphasize that these validation messages related to Bootstrap do not affect the functionality or performance of the Daily Finance Pulse project.

This experience aligns with the validation results observed during the walkthrough project, where Bootstrap-related error messages were also present. It's crucial to acknowledge that these messages are common when utilizing Bootstrap and do not imply any issues with the actual code or user experience.

Rest assured, I'm committed to adhering to HTML standards and resolving any valid structural errors that may arise during development, all while ensuring that Bootstrap's powerful features continue to enhance the overall user interface and experience.

[Validate Your HTML](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-dailyfinancepulse-bad0d88857ab.herokuapp.com%2F)


## CSS Validation (W3C CSS Validation Service)
THe custom CSS styles have undergone  validation using the W3C CSS Validation Service for CSS level 3 + SVG. This validation process ensures that the stylesheets adhere to industry standards, promoting consistent and reliable styling across the platform.

[Validate Your CSS](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpp4-dailyfinancepulse-bad0d88857ab.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

No errors where found:
![image](https://github.com/ZeroCool989/DailyFinancePulse-/assets/75548207/c89d5501-be17-4f8a-b835-b91a92dda590)

## Python Validation (PEP8)
All custom Python code files used in the Daily Finance Pulse project have been validated for compliance with PEP8, the Python Enhancement Proposal 8 style guide. This validation was performed both in the development environment and through online PEP8 validators. The use of `# noqa` comments in settings.py has been strategically employed where necessary to prevent line breaks from affecting Django functionality.

PEP8 Online Validation:
(https://www.pythonchecker.com/) 

Code pases the python validation check.


## JavaScript Validation (JSHint)
The minimal custom JavaScript code used in Daily Finance Pulse has undergone validation using JSHint. This validation process ensures that the JavaScript code adheres to best practices and maintains high code quality.

[JSHint Validation Screenshot] : 
![image](https://github.com/ZeroCool989/DailyFinancePulse-/assets/75548207/5401028c-5882-415e-b971-498bd74455c8)

# Credits and Acknowledgments

This project was greatly inspired by and relied upon various resources and services. Special thanks to all the platforms and communities that made this project possible.

## Walkthrough Project from Code Institute

A significant portion of this project was developed with guidance from the walkthrough projects provided by the [Code Institute](https://codeinstitute.net/). Their comprehensive educational materials were instrumental in the development of this project.

## Bootstrap

The project utilizes [Bootstrap](https://getbootstrap.com/) for its responsive design and prebuilt components, contributing greatly to the UI/UX design.

## Pexels

Images used in the project were sourced from [Pexels](https://www.pexels.com/), a free stock photo library, which greatly enhanced the visual appeal of the project.

## Cloudinary

[Cloudinary](https://cloudinary.com/) was used for efficient image and media management, allowing for optimized storage and delivery of the project's visual content.

## ElephantSQL

Database management was handled using [ElephantSQL](https://www.elephantsql.com/), providing a robust and scalable PostgreSQL database service.

## Additional Thanks

- A heartfelt thank you to the open-source community for various libraries and tools used in this project.
- Appreciation to all the developers and contributors of the third-party packages and plugins integrated into this project.
- Special mention to the online forums, blogs, and communities for their invaluable support and resources.

This project is a culmination of learning, inspiration, and support from these incredible resources. The knowledge and tools they provided were fundamental to the successful completion of this project.
