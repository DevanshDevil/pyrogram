#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import raw
from pyrogram.scaffold import Scaffold


class GetDialogsCount(Scaffold):
    async def get_dialogs_count(self, pinned_only: bool = False) -> int:
        """Get the total count of your dialogs.

        pinned_only (``bool``, *optional*):
            Pass True if you want to count only pinned dialogs.
            Defaults to False.

        Returns:
            ``int``: On success, the dialogs count is returned.

        Example:
            .. code-block:: python

                count = app.get_dialogs_count()
                print(count)
        """

        if pinned_only:
            return len((await self.send(raw.functions.messages.GetPinnedDialogs(folder_id=0))).dialogs)
        r = await self.send(
            raw.functions.messages.GetDialogs(
                offset_date=0,
                offset_id=0,
                offset_peer=raw.types.InputPeerEmpty(),
                limit=1,
                hash=0
            )
        )

        if isinstance(r, raw.types.messages.Dialogs):
            return len(r.dialogs)
        else:
            return r.count
