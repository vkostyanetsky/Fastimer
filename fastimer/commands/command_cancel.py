def cancel_fast() -> None:
    """
    Cancels the active fast.
    """

    pass


#
#     fasts = datafile.read_fasts()
#     active_fast = utils.get_active_fast(fasts)
#
#     if active_fast is not None:
#         cliutils.clear_terminal()
#
#         prompt = "Do you want to CANCEL the active fast? It cannot be undone."
#
#         if cliutils.ask_for_yes_or_no(prompt):
#             fasts.remove(active_fast)
#             datafile.write_fasts(fasts)
#
#     main_menu()
