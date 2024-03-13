from .database import get_database_connection


def get_vessel_count():
    try:
        db_conn = get_database_connection()
        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT COUNT(DISTINCT VesselID) AS total_vessels FROM vslvessels"
        )
        rows = cursor.fetchall()
        total_vessels = rows[0][0] if rows else 0
        return {"total_vessels": total_vessels}
    except pyodbc.Error as e:
        print(f"Error fetching vessel count: {e}")
        return None
    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()
