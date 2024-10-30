query_id = """
INSERT INTO `sp_manager` (`mg_id`,`mg_name`, `mg_pwd`, `mg_mobile`, `mg_email`, `mg_time`, `role_id`, `mg_state`) VALUES
  (2310,'谢玉兰', '123456789', '18032040387', 'yong45@example.com', 1729928045, -1, NULL)
"""
delete_id = """
DELETE FROM sp_manager WHERE mg_id = 2310
"""
delete_id_sql = """
DELETE FROM sp_manager WHERE mg_id = %s
"""