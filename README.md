# 🛠️ CTFd Score Adjustment API

A lightweight Flask route for **CTFd administrators** to manually adjust user or team scores via a secure API endpoint. Useful for:

- Awarding bonus points
- Penalizing teams
- Manual fixes after system issues
- Adjustments during Attack & Defense or PvC rounds

---

## 🚀 Features

- 🔐 Admin-only access using `@admins_only` decorator
- ✅ Supports both **user-based** and **team-based** score adjustments
- 📝 Custom reason/description for traceability
- 🕓 Timestamps score adjustment with UTC datetime

---

## 🧩 Endpoint

### GET /api/score/adjust`

> ⚠️ This route requires an **authenticated admin** session.

---

## 📥 Request (JSON body)

Send a JSON body with the following fields:

| Field     | Type     | Required | Description                                  |
|-----------|----------|----------|----------------------------------------------|
| `points`  | Integer  | ✅       | The number of points to add or subtract      |
| `user_id` | Integer  | ❌       | The ID of the user to award                  |
| `team_id` | Integer  | ❌       | The ID of the team to award                  |
| `reason`  | String   | ❌       | Reason for the adjustment (default provided) |

> Either `user_id` or `team_id` **must** be provided.

---

## 📤 Example Request

```json
{
  "team_id": 3,
  "points": 100,
  "reason": "Bonus for successful defense round"
}
