def main(path: str) -> None:
    """
    Starts a new fast.
    """

    pass


#
#     fasts = datafile.read_fasts()
#     fast = utils.get_active_fast(fasts)
#
#     if fast is not None:
#         print("Fast is already on.")
#         print()
#
#         cliutils.ask_for_enter()
#
#     else:
#         length = None
#
#         while length is None:
#             user_input = input("Enter fast duration in hours: ")
#
#             if user_input.isdigit():
#                 length = int(user_input)
#                 fast = {
#                     "length": length,
#                     "started": datetime.datetime.now(),
#                 }
#
#                 fasts.append(fast)
#
#                 datafile.write_fasts(fasts)
#
#             else:
#                 print("Please enter a valid number.")
#                 print()
