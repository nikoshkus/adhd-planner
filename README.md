# adhd-planner

ADHD Planner
My Day (Мій день): summary and plan
What it is

A task planner for people with ADHD. It builds a short, realistic list for today based on your mood, energy and available time, and reminds you of what matters. It started as a single-file web prototype and is now an Android app built with Capacitor and GitHub Actions.

What it does now

Tasks

Recurring templates (daily, weekly, monthly, yearly) that you can edit.
Each task has a time estimate, difficulty and importance, on word scales (“quick”, “hard”, “critical”).
Weekly, monthly and yearly tasks show their day, and lists are sorted by time.
Overdue weekly, monthly and yearly tasks carry over with a boost in priority.
“Skip this time” clears a task until its next scheduled occurrence.
Complex tasks are split into steps when you create them.

Daily flow

A morning check-in asks about mood, energy and available time, then picks matching tasks.
A “Don’t forget” block shows important or overdue tasks that didn’t fit the pick.
You can show the full list for today at any point.

AI (Gemini, free tier only)

Suggests time, difficulty, importance, reminder time and steps, and you can correct them.
Finds free models by testing each one, with timeouts and fallback to other models, then to a simple built-in estimate.

Calendar

On Android it reads the phone calendar, so multiple accounts work without any Google sign-in.
You choose which calendars to use, and duplicate meetings are counted once.
Busy time shrinks the day’s budget and flags tasks that clash with events.
It can write tasks into a chosen calendar as recurring events.
The browser version uses Google Calendar via OAuth.

Reminders and data

Android local notifications are scheduled 14 days ahead, with tasks at the same time grouped, and they work when the app is closed.
Data is stored on the device, with JSON export through the Android share sheet and import.
Status
The web logic was tested with simulated data. The Android build is signed, installed and running on your phone.
The recurring-events calendar fix is waiting for your confirmation.
Not yet verified on a real device: notification timing, reminders after reboot, and calendar writing.

Plan

1. Verify (next)

Install the latest build and check that recurring events show on the right day.
Run the 10-second notification test, set battery mode to “Unrestricted”, and confirm reminders still arrive the next morning.
Import your tasks from the prototype and try writing one task to the calendar.

2. Quick wins

Notification buttons for “Done” and “Snooze 10 min”.
A “Now” mode showing one next task.
Configurable day start and end (currently 07:00 to 22:00).
A custom app icon.

3. Next

Checkable steps within tasks, and a simple history of completed tasks.
A focus timer.
Automatic backups.
English and Ukrainian interface.

4. Later, if needed

Read calendar occurrences through a small native plugin, if the current one stays unreliable.
AI-suggested time slots around your events.
Risks to watch
The calendar plugin’s handling of recurring events.
Phone makers that delay notifications.
Free API limits changing.
Google’s developer verification rules for installing apps outside Play.
Losing the signing key. Keep myday.keystore and its password backed up.
