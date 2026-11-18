from app.modules import ooo_hop_insert


def list_primary(conn, waybill_id: str) -> list[dict]:
    """正式时间线读持久化点表 timeline_points：顺序在装载时已物化并维护，刷新后不乱序。"""
    return ooo_hop_insert.list_timeline_points(conn, waybill_id)
